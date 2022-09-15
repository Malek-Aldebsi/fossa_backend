from django.contrib import admin
from .models import StepsRecords, HeartRate, SleepHours

admin.site.register(StepsRecords)
admin.site.register(HeartRate)
admin.site.register(SleepHours)
