from django.db import models
from django.contrib.auth import get_user_model


class Gravity(models.Model):
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')
    z = models.FloatField(verbose_name='Z')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.x, self.y, self.z,)


class UserAcceleration(models.Model):
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')
    z = models.FloatField(verbose_name='Z')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.x, self.y, self.z,)


class Attitude(models.Model):
    roll = models.FloatField(verbose_name='X')
    pitch = models.FloatField(verbose_name='Y')
    yaw = models.FloatField(verbose_name='Z')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.roll, self.pitch, self.yaw,)


class MagneticField(models.Model):
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')
    z = models.FloatField(verbose_name='Z')
    accuracy = models.FloatField(verbose_name='Accuracy')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.x, self.y, self.z,)


class Location(models.Model):
    longitude = models.FloatField(verbose_name='Longitude')
    latitude = models.FloatField(verbose_name='Latitude')
    altitude = models.FloatField(verbose_name='Altitude')
    sat_timestamp = models.DateTimeField(verbose_name='Satellite Timestamp')
    horizontal_accuracy = models.FloatField(verbose_name='Horizontal Accuracy')
    vertical_accuracy = models.FloatField(verbose_name='Vertical Accuracy')
    speed = models.FloatField(verbose_name='Speed')
    course = models.FloatField(verbose_name='Course')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='User')

    def __str__(self):
        return "%d, %f, %f, %f" % (self.id, self.longitude, self.latitude, self.altitude)


