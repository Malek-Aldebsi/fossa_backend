# Generated by Django 4.1 on 2022-09-09 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_customuser_first_name_customuser_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
