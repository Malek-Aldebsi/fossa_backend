from django.db import models
from user_profile.models import CustomUser


class StepsRecords(models.Model):
    num_of_steps = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)


class HeartRate(models.Model):
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)


class SleepHours(models.Model):
    num_of_sleep_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)
