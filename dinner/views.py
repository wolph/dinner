from django.conf import settings
from django_utils import view_decorators
from . import forms
from . import models
from . import utils
import datetime
import itertools
import functools


def parse_date(f):
    @functools.wraps(f)
    def _parse_date(*args, **kwargs):
        date = kwargs.get('date')
        begin_date, end_date = utils.get_days_range(
            days=settings.DEFAULT_DINNER_DAYS)

        if isinstance(date, basestring):
            date = datetime.date(*map(int, date.split('-')))
        elif not isinstance(date, datetime.date):
            date = datetime.date.today()

        kwargs['date'] = max(begin_date, min(date, end_date))
        kwargs['begin_date'] = begin_date
        kwargs['end_date'] = end_date

        return f(*args, **kwargs)
    return _parse_date


@view_decorators.env
@parse_date
def index(request, date, begin_date, end_date):
    done = False
    data = request.POST or None

    if isinstance(request.session.get('reservations'), dict):
        user_reservations = request.session['reservations']
    else:
        user_reservations = request.session['reservations'] = dict()

    # Create new reservations
    create_form = forms.ReservationCreateForm(
        formdata=data,
        user=request.user,
        dinners=models.Dinner.objects.get_days(begin_date, end_date),
    )
    if not done and data and create_form.validate():
        reservations = create_form.save()
        for reservation in reservations:
            user_reservations[reservation.pk] = reservation

        if reservations:
            done = True
            request.session.modified = True
            if not request.ajax:
                return request.redirect()

    # Get the existing reservations
    reservations = models.Reservation.objects.get_days(begin_date, end_date)
    if request.user.is_authenticated():
        for reservation in reservations:
            if reservation.user == request.user:
                user_reservations[reservation.pk] = reservation

    # Remove reservations when asked
    remove_form = forms.get_reservation_remove_form(
        reservations=reservations,
        user=request.user,
        user_reservations=user_reservations,
        formdata=data,
    )
    if not done and data and remove_form.validate():
        for reservation in remove_form.save():
            user_reservations.pop(reservation.pk, None)

        request.session.modified = True
        if request.ajax:
            return request.redirect()

    days = utils.get_days(begin_date, end_date - datetime.timedelta(days=1))
    reservations_per_day = dict(
        (k, list(vs)) for k, vs in
        itertools.groupby(reservations, lambda r: r.dinner.date))
    reservations = []
    for day in days:
        # Get all reservations per day
        reservations.append((day, reservations_per_day.get(day, [])))

    request.context['create_form'] = create_form
    request.context['remove_form'] = remove_form
    request.context['reservations'] = reservations
    request.context['user_reservations'] = set(user_reservations)
    request.context['date'] = date

