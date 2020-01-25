from django.contrib import admin
from .models import Gravity, UserAcceleration, Attitude, MagneticField, Location

admin.site.site_header = "Telemetry Django Server"

@admin.register(Gravity)
class GravityAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'z', ]
    readonly_fields = ['id', 'user', 'created', ]
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


@admin.register(UserAcceleration)
class UserAccelerationAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'z', ]
    readonly_fields = ['id', 'user', 'created', ]
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


@admin.register(Attitude)
class AttitudeAdmin(admin.ModelAdmin):
    fields = ['roll', 'pitch', 'yaw', ]
    readonly_fields = ['id', 'user', 'created', ]
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


@admin.register(MagneticField)
class MagneticFieldAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'z', 'accuracy', ]
    readonly_fields = ['id', 'user', 'created', ]
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


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = [
            'longitude', 'latitude', 'altitude', 'timestamp', 'sat_timestamp',
            'horizontal_accuracy', 'vertical_accuracy', 'speed', 'course', 
        ]
    readonly_fields = ['id', 'user', 'created', ]
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
