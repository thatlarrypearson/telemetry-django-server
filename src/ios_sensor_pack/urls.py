# urls.py
from django.urls import path
from django.views.generic import TemplateView
#from .views import GravityList, GravityDetail, UserAccelerationList, UserAccelerationDetail
from .views import (
    GravityViewSet, UserAccelerationViewSet, AttitudeViewSet, MagneticFieldViewSet, LocationViewSet, IosSensorViewSet
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="sensorpack-index.html"), name='index'),

    path('gravity/', GravityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('gravity/<int:pk>/', GravityViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy',
                                            })
    ),

    path('user_acceleration/', UserAccelerationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user_acceleration/<int:pk>/', UserAccelerationViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy'
                                            })),

    path('attitude/', AttitudeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('attitude/<int:pk>/', AttitudeViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy'
                                            })),

    path('magnetic_field/', MagneticFieldViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('magnetic_field/<int:pk>/', MagneticFieldViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy'
                                            })),

    path('location/', LocationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('location/<int:pk>/', LocationViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy'
                                            })),

    path('ios_sensor/', IosSensorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('ios_sensor/<int:pk>/', IosSensorViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy'
                                            })),

]