from django.conf import settings
import wtforms
import wtformsparsleyjs
import models
from django.utils.translation import ugettext as _


class BootstrapButtonWidgetBase(wtforms.widgets.SubmitInput):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        kwargs.setdefault('type', 'submit')
        kwargs.setdefault('class', 'btn btn-small')

        if kwargs.pop('disabled', False):
            kwargs['disabled'] = 'disabled'

        icon = kwargs.pop('icon', 'ban-circle')

        return wtforms.widgets.HTMLString(
            '''
            <button %(button_kwargs)s>
                %(label)s
                <span class="glyphicon glyphicon-%(icon)s"></span>
            </button>
            '''
            % dict(
                button_kwargs=self.html_params(**kwargs),
                label=field.label.text,
                icon=icon,
            )
        )


class BootstrapAddButtonWidget(BootstrapButtonWidgetBase):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', 'btn btn-success btn-small')
        kwargs.setdefault('icon', 'plus')

        return BootstrapButtonWidgetBase.__call__(self, field, **kwargs)


class BootstrapRemoveButtonWidget(BootstrapAddButtonWidget):
    def __call__(self, field, **kwargs):
        field.label.text = ''
        kwargs.setdefault('class', 'btn btn-danger btn-small')
        kwargs.setdefault('icon', 'remove')

        return BootstrapButtonWidgetBase.__call__(self, field, **kwargs)


class BootstrapButtonsWidget(object):
    def __call__(self, field, **kwargs):
        button_kwargs = kwargs.pop('button', {})
        button_kwargs['disabled'] = kwargs.pop('disabled', False)
        kwargs.setdefault('id', field.id)
        html = ['<div %s>' % wtforms.widgets.html_params(**kwargs)]

        for button in field:
            html.append(button(**button_kwargs))

        html.append('</div>')
        return wtforms.widgets.HTMLString(''.join(html))


class BootstrapAddButtonsField(wtforms.SelectMultipleField):
    widget = BootstrapButtonsWidget()
    option_widget = BootstrapAddButtonWidget()


class BootstrapRemoveButtonsField(wtforms.SelectMultipleField):
    widget = BootstrapButtonsWidget()
    option_widget = BootstrapRemoveButtonWidget()


def not_expired(form, field, message=_('Het is helaas niet meer mogelijk je '
                                       'in te schrijven voor dit diner.')):
    dinner = getattr(field, 'dinner', None)
    if field.data and (not dinner or dinner.is_expired):
        raise wtforms.ValidationError(message)


class DailyCourseMeta(wtforms.form.FormMeta):
    '''Metaclass to automatically generate a course for each day, probably
    overkill but easier to modify this way'''
    def __new__(meta, name, bases, dict_):
        for day in range(settings.DEFAULT_DINNER_DAYS):
            dict_['course_%d' % day] = BootstrapAddButtonsField(
                choices=[],
                coerce=int,
                validators=[not_expired],
            )

        return wtforms.form.FormMeta.__new__(meta, name, bases, dict_)


class ReservationCreateForm(wtforms.Form):
    __metaclass__ = DailyCourseMeta
    name = wtformsparsleyjs.StringField(_('Name'), validators=[
        wtformsparsleyjs.Length(3, 100),
    ])
    email = wtformsparsleyjs.StringField(_('Email'), validators=[
        wtformsparsleyjs.Email(_('Sorry, not a valid email address.')),
        wtformsparsleyjs.Length(3, 75),
    ])
    comment = wtforms.StringField(_('Opmerkingen'))

    def __init__(self, user, dinners, formdata=None, obj=None, prefix='',
                 *args, **kwargs):
        self.user = user
        self.dinners = dinners
        self.courses = {}

        wtforms.Form.__init__(self, formdata=formdata, obj=obj, prefix=prefix,
                              **kwargs)

        for day, dinner in enumerate(dinners):
            course_radio = getattr(self, 'course_%d' % day)
            course_radio.label.text = dinner.date.strftime('%A')
            course_radio.choices = []
            course_radio.dinner = dinner

            dinner.field = course_radio

            for course in dinner.courses.all():
                self.courses[course.pk] = course
                course_radio.choices.append((
                    course.pk, course.name,
                ))

    def save(self):
        data = self.data
        kwargs = dict(
            user=self.user.is_authenticated() and self.user or None,
            name=data['name'],
            email=data['email'],
            comments=data['comment'],
        )

        reservations = []
        for dinner in self.dinners:
            # We won't add dinner reservations after 14:00 in the afternoon
            if dinner.is_expired:
                continue

            values = self.data[dinner.field.name]
            for value in values:
                reservations.append(models.Reservation.objects.create(
                    dinner=dinner,
                    course=self.courses[value],
                    **kwargs))

        return reservations


class ReservationRemoveForm(wtforms.Form):
    def __init__(self, user, user_reservations, reservations, *args, **kwargs):
        self.user = user
        self.user_reservations = user_reservations
        self.reservations = reservations

        wtforms.Form.__init__(self, *args, **kwargs)

    def save(self):
        data = self.data
        ids = set()
        for k, vs in data.iteritems():
            if k.startswith('reservation_'):
                ids |= set(vs)

        for id_ in ids.copy():
            reservation = self.user_reservations.get(id_)
            if reservation:
                ids.remove(id_)
                reservation.delete()
                yield reservation

        if self.user.is_staff:
            for reservation in models.Reservation.objects.filter(pk__in=ids):
                reservation.delete()
                yield reservation


def get_reservation_remove_form(user, user_reservations, reservations,
                                formdata=None):
    class UserReservationRemoveForm(ReservationRemoveForm):
        pass

    for i, reservation in enumerate(reservations):
        field = BootstrapRemoveButtonsField(
            choices=[(reservation.pk, reservation.pk)],
            coerce=int,
            validators=[not_expired],
        )
        setattr(UserReservationRemoveForm, 'reservation_%d' % i, field)

    form = UserReservationRemoveForm(user, user_reservations, reservations,
                                     formdata=formdata)

    for i, reservation in enumerate(reservations):
        reservation.field = getattr(form, 'reservation_%d' % i)
        reservation.field.dinner = reservation.dinner

    return form

