from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils import safestring
import datetime
from . import utils


class DinnerManager(models.Manager):
    def get_days(self, date=None):
        start_date, end_date = utils.get_days_range(date)
        days = utils.get_days_from(date, 5)

        dinners = dict((d.date, d) for d in self.filter(
            date__gte=start_date,
            date__lt=end_date,
        ))

        for day in days:
            if day in dinners:
                yield dinners[day]
            else:
                yield Dinner(date=day)


class Dinner(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cooks = models.ManyToManyField('auth.User', blank=True)
    date = models.DateField(default=datetime.date.today)
    price = models.DecimalField(default=settings.DEFAULT_DINER_PRICE,
                                max_digits=8, decimal_places=2)

    objects = DinnerManager()

    @property
    def is_expired(self):
        end_time = datetime.datetime.combine(self.date, datetime.time(16))
        now = datetime.datetime.now()
        return end_time < now

    def get_cooks(self):
        if self.pk:
            return u', '.join(unicode(c) for c in self.cooks.all())
        else:
            return _('Onbekend')

    def get_description(self):
        description = []
        if self.description:
            description.append(self.description)

        for course in self.courses.all().order_by('number'):
            if course.description and course.name:
                description.append('%s: %s' % (
                    course.name, course.description))
            elif course.description:
                description.append(course.description)

        if not description:
            return safestring.mark_safe('&nbsp;')

        return ', '.join(description)

    def __repr__(self):
        return '<%s[%s] %s>' % (
            self.__class__.__name__,
            self.date,
            self.name,
        )

    class Meta:
        unique_together = (
            ('date',),
        )


class Course(models.Model):
    dinner = models.ForeignKey(Dinner, related_name='courses')
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (
            ('dinner', 'name', 'number'),
        )


class Reservation(models.Model):
    user = models.ForeignKey('auth.User', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(Course)
    paid = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=8, decimal_places=2)

