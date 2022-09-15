from django.urls import path
from . import views

urlpatterns = [
    path('', views.build_profile),
    path('check/', views.check_user),
]
