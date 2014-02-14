from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django_utils import base_models
import datetime
from . import utils


class CourseManager(models.Manager):
    def default(self):
        return self.filter(default=True)


class DinnerManager(models.Manager):
    def get_days(self, begin_date, end_date):
        days = utils.get_days(begin_date, end_date)

        dinners = dict((d.date, d) for d in self.filter(
            date__gte=begin_date,
            date__lt=end_date,
        ))

        for day in days[:-1]:
            if day in dinners:
                yield dinners[day]
            else:
                dinner = Dinner(date=day)
                dinner.save()
                dinner.courses.add(
                    *Course.objects.default().values_list('pk', flat=True))
                dinner.save()
                yield dinner


class ReservationManager(models.Manager):
    def get_days(self, begin_date, end_date):
        return self.filter(
            dinner__date__gte=begin_date,
            dinner__date__lt=end_date,
        ).order_by('dinner__date')[:]


class Dinner(base_models.ModelBase):
    description = models.TextField(blank=True, default='')
    cooks = models.ManyToManyField('auth.User')
    date = models.DateField(default=datetime.date.today)
    price = models.DecimalField(
        default=settings.DEFAULT_DINNER_PRICE, max_digits=8, decimal_places=2)
    cost = models.DecimalField(
        default=settings.DEFAULT_DINNER_COST, max_digits=8, decimal_places=2)
    courses = models.ManyToManyField('Course', related_name='dinner')
    objects = DinnerManager()

    @property
    def is_expired(self):
        end_time = datetime.datetime.combine(self.date, settings.DINNER_SIGNUP_UNTIL)
        now = datetime.datetime.now()
        return end_time < now

    def get_cooks(self):
        cooks = None
        if self.pk:
            cooks = list(self.cooks.all().values_list('username', flat=True))

        if cooks:
            return u', '.join(cooks)
        else:
            return _('Onbekend')
    get_cooks.short_description = 'Cooks'

    def get_courses(self):
        if self.pk:
            return u', '.join(unicode(c) for c in self.courses.all())
        else:
            return _('Onbekend')
    get_courses.short_description = 'Courses'

    def __repr__(self):
        return '<%s[%s]>' % (
            self.__class__.__name__,
            self.date,
        )

    def __unicode__(self):
        return unicode(self.date)

    class Meta:
        unique_together = (
            'date',
        )
        ordering = ['date']


class Course(base_models.ModelBase):
    name = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    objects = CourseManager()

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = (
            'name',
        )


class Reservation(base_models.NameMixin, base_models.ModelBase):
    user = models.ForeignKey('auth.User', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField(null=True, blank=True)
    dinner = models.ForeignKey(Dinner)
    course = models.ForeignKey(Course)
    paid = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    objects = ReservationManager()

    def __repr__(self):
        return (u'<%s[%s] %s: %s>' % (
            self.__class__.__name__,
            getattr(self, 'pk', '?'),
            self.name,
            self.dinner.date,
        )).encode('utf-8')

    def __unicode__(self):
        return '%s (%s) for %s' % (self.dinner, self.course, self.name)

    class Meta:
        ordering = ['dinner__date',]

