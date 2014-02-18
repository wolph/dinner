import models
from koornbeurs import models as koornbeurs_models
from django.contrib import admin
from django.conf import settings
from django.utils import functional
from tags_input import admin as tags_input_admin
import reversion


class AdminSite(admin.AdminSite):
    def has_permission(self, request):
        print 'has permission', request
        return bool(koornbeurs_models.Group.objects.koks().filter(
            users__username='Magnix',
            #users__username=request.user.username,
        ).count())

site = AdminSite('dinner_admin', app_name='dinner_admin')


class CourseAdmin(reversion.VersionAdmin):
    list_display = ('name', 'default')
    list_editable = ('default',)
    list_filter = ('dinner',)
    search_fields = ('name',)


class CourseInline(admin.TabularInline):
    model = models.Course
    extra = len(settings.DEFAULT_DINNER_COURSES) + 2

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.courses.count():
            return 1
        else:
            return admin.TabularInline.get_extra(self, request, obj, **kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == 'GET' and (not obj or not obj.courses.count()):
            for i, course in enumerate(settings.DEFAULT_DINNER_COURSES, 1):
                for k, v in course.iteritems():
                    initial.append({
                        'number': i,
                        'name': k,
                        'description': v,
                    })

        formset = super(CourseInline, self).get_formset(request, obj, **kwargs)
        formset.__init__ = functional.curry(formset.__init__, initial=initial)
        return formset


class DinnerAdmin(reversion.VersionAdmin, tags_input_admin.TagsInputAdmin):
    list_display = ('date', 'get_cooks', 'get_courses', 'description', 'price',
                    'cost',)
    list_filter = ('date', 'courses')
    raw_id_fields = ('cooks',)
    search_fields = ('description', 'cooks__username', 'courses__name')
    list_editable = ['description', 'price']

    def add_view(self, request, form_url='', extra_context=None):
        data = request.GET.copy()
        data.setdefault('cooks', str(request.user.username))
        data.setdefault('courses', ','.join(
            models.Course.objects.default().values_list('name', flat=True)))
        request.GET = data
        return super(DinnerAdmin, self).add_view(
            request=request, form_url=form_url, extra_context=extra_context)


class ReservationAdmin(reversion.VersionAdmin):
    list_display = (u'id', 'user', 'name', 'email', 'comments', 'paid')
    list_filter = ('user',)
    raw_id_fields = ('course', 'dinner')
    search_fields = ('name',)


def _register(model, admin_class):
    if model not in site._registry:
        site.register(model, admin_class)

    if model not in admin.site._registry:
        admin.site.register(model, admin_class)


_register(models.Course, CourseAdmin)
_register(models.Dinner, DinnerAdmin)
_register(models.Reservation, ReservationAdmin)

