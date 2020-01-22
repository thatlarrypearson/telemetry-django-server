# serializers.py
from datetime import datetime
from rest_framework import serializers
from .models import Gravity, UserAcceleration, Attitude, MagneticField, Location


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

