from django.conf import settings
from django_utils import view_decorators
from . import forms
from . import models
from . import utils
import datetime
import itertools


@view_decorators.env
def index(request, date=datetime.date.today()):
    begin_date, end_date = utils.get_days_range(
        days=settings.DEFAULT_DINNER_DAYS)
    data = request.POST or None
    if isinstance(request.session.get('reservations'), dict):
        user_reservations = request.session['reservations']
    else:
        user_reservations = request.session['reservations'] = dict()

    dinners = list(models.Dinner.objects.get_days(begin_date, end_date))
    create_form = forms.ReservationCreateForm(
        formdata=data,
        user=request.user,
        dinners=dinners,
    )
    if data and create_form.validate():
        reservations = create_form.save()
        for reservation in reservations:
            user_reservations[reservation.pk] = reservation

        if reservations:
            request.session.modified = True
            return request.redirect()
    elif create_form.errors:
        print 'errors', create_form.errors

    date = max(begin_date, min(datetime.date.today(), end_date))
    reservations = models.Reservation.objects.get_days(begin_date, end_date)
    if request.user.is_authenticated():
        for reservation in reservations:
            if reservation.user == request.user:
                user_reservations[reservation.pk] = reservation

    remove_form = forms.get_reservation_remove_form(
        reservations=reservations,
        user=request.user,
        user_reservations=user_reservations,
        formdata=data,
    )

    if data and remove_form.validate():
        for reservation in remove_form.save():
            user_reservations.pop(reservation.pk, None)

        request.session.modified = True
        return request.redirect()

    days = utils.get_days(begin_date, end_date - datetime.timedelta(days=1))
    reservations_per_day = dict(
        itertools.groupby(reservations, lambda r: r.dinner.date))

    reservations = []
    for day in days:
        reservations.append((day, list(reservations_per_day.get(day, []))))

    request.context['create_form'] = create_form
    request.context['remove_form'] = remove_form
    request.context['reservations'] = reservations
    request.context['user_reservations'] = set(user_reservations)
    request.context['date'] = date


@view_decorators.env
def remove(request):
    data = request.POST or None

    form = forms.DinnerForm(
        formdata=data,
    )

    request.context['form'] = form

