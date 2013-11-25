import models
from django.contrib import admin
from django.conf import settings
from django.utils import functional


class CourseAdmin(admin.ModelAdmin):
    list_display = (u'id', 'dinner', 'name', 'number', 'description')
    list_filter = ('dinner',)
    search_fields = ('name',)
    list_editable = ['name', 'number', 'description']


class CourseInline(admin.TabularInline):
    model = models.Course
    extra = len(settings.DEFAULT_DINER_COURSES) + 2

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.courses.count():
            return 1
        else:
            return admin.TabularInline.get_extra(self, request, obj, **kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == 'GET' and (not obj or not obj.courses.count()):
            for i, course in enumerate(settings.DEFAULT_DINER_COURSES, 1):
                for k, v in course.iteritems():
                    initial.append({
                        'number': i,
                        'name': k,
                        'description': v,
                    })

        formset = super(CourseInline, self).get_formset(request, obj, **kwargs)
        formset.__init__ = functional.curry(formset.__init__, initial=initial)
        return formset


class DinnerAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    list_display = (u'id', 'name', 'description', 'date', 'price')
    list_filter = ('date',)
    raw_id_fields = ('cooks',)
    search_fields = ('name',)
    list_editable = ['name', 'description', 'price']

    def add_view(self, request, form_url='', extra_context=None):
        data = request.GET.copy()
        data.setdefault('cooks', str(request.user.pk))
        request.GET = data
        return super(DinnerAdmin, self).add_view(
            request=request, form_url=form_url, extra_context=extra_context)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (u'id', 'user', 'name', 'email', 'comments', 'paid')
    list_filter = ('user',)
    raw_id_fields = ('courses',)
    search_fields = ('name',)


def _register(model, admin_class):
    if model not in admin.site._registry:
        admin.site.register(model, admin_class)

_register(models.Course, CourseAdmin)
_register(models.Dinner, DinnerAdmin)
_register(models.Reservation, ReservationAdmin)

