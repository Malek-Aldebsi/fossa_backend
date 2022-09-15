from django.urls import path
from . import views

urlpatterns = [
    path('', views.build_examinations_record),
]
