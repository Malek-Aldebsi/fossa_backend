from django.contrib import admin

from .models import CustomUser, PetKind, Pet

admin.site.register(CustomUser)
admin.site.register(PetKind)
admin.site.register(Pet)
