from django.contrib import admin
from .models import Gravity, UserAcceleration, Attitude, MagneticField

admin.site.site_header = "Example 1: Sensor Pack"

@admin.register(Gravity)
class HeroAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'z', ]
    readonly_fields = ['id', ]
    exclude = None


@admin.register(UserAcceleration)
class UserAccelerationAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'z', ]
    readonly_fields = ['id', 'user', ]
    exclude = None

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

    def queryset(self, request):
        if request.user.is_superuser:
            qs = self.model._default_manager.all()
        else:
            qs = self.model._default_manager.filter(user=request.user)
        return qs