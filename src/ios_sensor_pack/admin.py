from django.contrib import admin
from .models import Gravity, UserAcceleration, Attitude, MagneticField, Location, IosSensor

admin.site.site_header = "Telemetry Django Server"

@admin.register(Gravity)
class GravityAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'z', ]
    readonly_fields = ['id', 'user', 'created', ]
    exclude = None
    list_filter = ['id', 'user', 'created', ]

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
    list_filter = ['id', 'user', 'created', ]

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
    list_filter = ['id', 'user', 'created', ]

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
    list_filter = ['id', 'user', 'created', ]

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
    list_filter = ['id', 'user', 'created', ]

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

@admin.register(IosSensor)
class IosSensorAdmin(admin.ModelAdmin):
    fields = [
            'gravity_x', 'gravity_y', 'gravity_z',

            'acceleration_x', 'acceleration_y', 'acceleration_z',

            'attitude_roll', 'attitude_pitch', 'attitude_yaw',

            'magnetic_x', 'magnetic_y', 'magnetic_z', 'magnetic_accuracy',

            'location_longitude', 'location_latitude', 'location_altitude',
            'location_timestamp', 'location_sat_timestamp',
            'location_horizontal_accuracy', 'location_vertical_accuracy',
            'location_speed', 'location_course', 
        ]
    readonly_fields = ['id', 'user', 'created', ]
    exclude = None
    list_filter = ['id', 'user', 'created', ]

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
