# Generated by Django 4.1 on 2022-09-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_examinations_records', '0002_alter_medicalexaminationsrecords_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalexaminationsrecords',
            name='lab_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
