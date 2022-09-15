from django.urls import path
from . import views

urlpatterns = [
    path('step_records/', views.step_records),
    path('last_records/', views.last_records),
    path('heart_rate/', views.heart_rate),
    path('sleep_hours/', views.sleep_hours),
    path('calculate_calories/', views.calculate_calories)
]
