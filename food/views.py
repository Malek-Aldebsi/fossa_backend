from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_profile.models import CustomUser
from .models import StepsRecords


@api_view(['POST'])
def step_records(request):
    data = request.data

    user = request.user
    user_profile = CustomUser.objects.get(
        user=user,
    )

    StepsRecords.objects.create(
        num_of_steps=data['num_of_steps'],
        date=data['date'],
        user=user_profile,
    )

    return Response()
