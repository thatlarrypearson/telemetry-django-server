# telemetry-django-server/src/ios_seensor_pack/models.py
import pytz
from datetime import datetime, timezone
from astropy.time import Time
from django.db import models
from django.contrib.auth import get_user_model


class Gravity(models.Model):
    id = models.BigAutoField(primary_key=True)
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')
    z = models.FloatField(verbose_name='Z')

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.x, self.y, self.z,)


class UserAcceleration(models.Model):
    id = models.BigAutoField(primary_key=True)
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')
    z = models.FloatField(verbose_name='Z')

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.x, self.y, self.z,)


class Attitude(models.Model):
    id = models.BigAutoField(primary_key=True)
    roll = models.FloatField(verbose_name='X')
    pitch = models.FloatField(verbose_name='Y')
    yaw = models.FloatField(verbose_name='Z')

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.roll, self.pitch, self.yaw,)


class MagneticField(models.Model):
    id = models.BigAutoField(primary_key=True)
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')
    z = models.FloatField(verbose_name='Z')
    accuracy = models.FloatField(verbose_name='Accuracy')

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.x, self.y, self.z,)


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    longitude = models.FloatField(verbose_name='Longitude')
    latitude = models.FloatField(verbose_name='Latitude')
    altitude = models.FloatField(verbose_name='Altitude')
    timestamp = models.DecimalField(verbose_name='Unprocessed IOS Timestamp', max_digits=20, decimal_places=7)
    horizontal_accuracy = models.FloatField(verbose_name='Horizontal Accuracy')
    vertical_accuracy = models.FloatField(verbose_name='Vertical Accuracy')
    speed = models.FloatField(verbose_name='Speed')
    course = models.FloatField(verbose_name='Course')

    sat_timestamp = models.DateTimeField(verbose_name='Satellite Timestamp')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def save(self, *args, **kwargs): 
        t = Time(str(self.timestamp), format='unix')
        self.sat_timestamp = pytz.utc.localize(t.to_datetime())
        super(Location, self).save(*args, **kwargs) 

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.longitude, self.latitude, self.altitude)


