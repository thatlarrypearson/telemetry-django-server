# serializers.py
from datetime import datetime
from rest_framework import serializers
from .models import Gravity, UserAcceleration, Attitude, MagneticField, Location, IosSensor


class GravitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Gravity
        fields = ['id', 'x', 'y', 'z', 'user', ]
        read_only_fields = ['created', 'user', ]


class UserAccellerationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserAcceleration
        fields = ['id', 'x', 'y', 'z', 'user', ]
        read_only_fields = ['created', 'user', ]

class AttitudeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Attitude
        fields = ['id', 'roll', 'pitch', 'yaw', 'user']
        read_only_fields = ['created', 'user', ]

class MagneticFieldSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MagneticField
        fields = ['id', 'x', 'y', 'z', 'accuracy', 'user', ]
        read_only_fields = ['created', 'user', ]


class LocationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Location
        fields = [
            'id', 'longitude', 'latitude', 'timestamp', 'altitude',
            'horizontal_accuracy', 'vertical_accuracy', 'speed', 'course',
            'sat_timestamp', 'created', 'user',
        ]
        read_only_fields = ['sat_timestamp', 'created', 'user', ]


class IosSensorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = IosSensor
        fields = [
            'id',

            'gravity_x', 'gravity_y', 'gravity_z',

            'acceleration_x', 'acceleration_y', 'acceleration_z',

            'attitude_roll', 'attitude_pitch', 'attitude_yaw',

            'magnetic_x', 'magnetic_y', 'magnetic_z', 'magnetic_accuracy',
            
            'location_longitude', 'location_latitude', 'location_timestamp', 'location_altitude',
            'location_horizontal_accuracy', 'location_vertical_accuracy', 'location_speed', 'location_course',
            'location_sat_timestamp',
            
            'created', 'user',
        ]
        read_only_fields = ['location_sat_timestamp', 'created', 'user', ]

