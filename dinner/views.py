from django_utils import view_decorators
from . import models
from . import forms


@view_decorators.env
def index(request):
    data = request.POST or None

    dinners = list(models.Dinner.objects.get_days())
    form = forms.ReservationForm(
        formdata=data,
        user=request.user,
        dinners=dinners,
    )

    request.context['form'] = form


@view_decorators.env
def create(request):
    data = request.POST or None

    form = forms.DinnerForm(
        formdata=data,
    )

    request.context['form'] = form

