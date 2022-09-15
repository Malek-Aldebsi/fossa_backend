from django.db import models
from user_profile.models import CustomUser


class MedicalExaminationsType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class MedicalExaminationsRecords(models.Model):
    measurement = models.IntegerField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    lab_name = models.CharField(max_length=200, null=True, blank=True)
    medical_examinationsType = models.ForeignKey(MedicalExaminationsType, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(CustomUser, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.medical_examinationsType.name}_{str(self.measurement)}"
