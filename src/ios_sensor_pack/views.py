from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Gravity, UserAcceleration, Attitude, MagneticField, Location
from .serializers import GravitySerializer, UserAccellerationSerializer, AttitudeSerializer, MagneticFieldSerializer, LocationSerializer


class GravityViewSet(viewsets.ModelViewSet):
    serializer_class = GravitySerializer
    model = Gravity
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = self.model._default_manager.all()
        else:
            qs = self.model._default_manager.filter(user=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAccelerationViewSet(viewsets.ModelViewSet):
    serializer_class = UserAccellerationSerializer
    model = UserAcceleration
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = self.model._default_manager.all()
        else:
            qs = self.model._default_manager.filter(user=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AttitudeViewSet(viewsets.ModelViewSet):
    serializer_class = AttitudeSerializer
    model = Attitude
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = self.model._default_manager.all()
        else:
            qs = self.model._default_manager.filter(user=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MagneticFieldViewSet(viewsets.ModelViewSet):
    serializer_class = MagneticFieldSerializer
    model = MagneticField
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = self.model._default_manager.all()
        else:
            qs = self.model._default_manager.filter(user=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    model = Location
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = self.model._default_manager.all()
        else:
            qs = self.model._default_manager.filter(user=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

