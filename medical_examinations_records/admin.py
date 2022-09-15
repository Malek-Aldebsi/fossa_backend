from django.contrib import admin

from .models import MedicalExaminationsType, MedicalExaminationsRecords

admin.site.register(MedicalExaminationsType)
admin.site.register(MedicalExaminationsRecords)
