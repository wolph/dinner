import models
from koornbeurs import models as koornbeurs_models
from django.contrib import admin
from django.conf import settings
from django.utils import functional
from tags_input import admin as tags_input_admin
from django import forms
import reversion


class AdminSite(admin.AdminSite):
    def has_permission(self, request):
        is_cook = bool(
            koornbeurs_models.Group.objects
            .cooks()
            .filter(users__username=request.user.username)
            .count()
        )
        return request.user.is_superuser or is_cook

site = AdminSite('dinner_admin', app_name='admin')


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


class ReservationInline(admin.TabularInline):
    model = models.Reservation
    readonly_fields = ('user', 'email',)
    fields = (
        'name',
        'paid',
        'comments',
    )
    formfield_overrides = {
        models.models.TextField: {'widget': forms.TextInput},
    }


class DinnerAdmin(reversion.VersionAdmin, tags_input_admin.TagsInputAdmin):
    list_display = ('date', 'get_cooks', 'get_courses', 'description', 'price',
                    'cost',)
    list_filter = ('date', 'courses')
    raw_id_fields = ('cooks',)
    search_fields = ('description', 'cooks__username', 'courses__name')
    list_editable = ['description', 'price']
    save_on_top = True

    inlines = [ReservationInline]

    def add_view(self, request, form_url='', extra_context=None):
        data = request.GET.copy()
        data.setdefault('cooks', str(request.user.username))
        data.setdefault('courses', ','.join(
            models.Course.objects.default().values_list('name', flat=True)))
        request.GET = data
        return super(DinnerAdmin, self).add_view(
            request=request, form_url=form_url, extra_context=extra_context)

    def get_form(self, request, obj=None, **kwargs):
        cooks = request.POST.get('cooks', '')
        if cooks:
            webgui_users = koornbeurs_models.User.objects.filter(
                username__in=cooks.split(','))

            for webgui_user in webgui_users:
                webgui_user.get_django_user()

        return super(DinnerAdmin, self).get_form(request, obj=obj, **kwargs)


class ReservationAdmin(reversion.VersionAdmin):
    list_display = (u'id', 'user', 'name', 'email', 'comments', 'paid',
                    'dinner')
    list_filter = ('user',)
    raw_id_fields = ('course', 'dinner')
    search_fields = ('name',)


def _register(model, admin_class):
    if model not in admin.site._registry:
        admin.site.register(model, admin_class)

    if model not in site._registry:
        site.register(model, admin_class)


_register(models.Course, CourseAdmin)
_register(models.Dinner, DinnerAdmin)
_register(models.Reservation, ReservationAdmin)

