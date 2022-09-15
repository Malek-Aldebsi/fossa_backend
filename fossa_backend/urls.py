from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'POST': '/api/build_profile/'},
        {'POST': '/api/examinations_record/'},
        {'POST': '/api/activities/'}
    ]

    return Response(routes)


urlpatterns = [
    path('', get_routes),
    path('admin/', admin.site.urls),
    path('api/build_profile/', include('user_profile.urls')),
    path('api/examinations_record/', include('medical_examinations_records.urls')),
    path('api/activities/', include('activities.urls')),
]
