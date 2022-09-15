from datetime import timedelta

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_profile.models import CustomUser
from .models import StepsRecords, HeartRate, SleepHours


@api_view(['POST'])
def step_records(request):
    data = request.data

    user_profile = CustomUser.objects.get(
        account=data['account'],
    )

    StepsRecords.objects.create(
        num_of_steps=data['num_of_steps'],
        date=data['date'],
        user=user_profile,
    )

    return Response()


@api_view(['POST'])
def last_records(request):
    data = request.data

    user_profile = CustomUser.objects.get(
        account=data['account'],
    )

    today_date = data['today_date']

    step_records = []

    day_1 = StepsRecords.objects.filter(user=user_profile).get(date=today_date)
    step_records.append(day_1.num_of_steps)

    date = day_1.date

    for i in range(5):
        date -= timedelta(days=1)
        record = StepsRecords.objects.filter(user=user_profile).get(date=date)
        step_records.append(record.num_of_steps)

    return Response(step_records)


@api_view(['POST'])
def heart_rate(request):
    data = request.data

    user_profile = CustomUser.objects.get(
        account=data['account'],
    )

    HeartRate.objects.create(
        heart_rate=data['heart_rate'],
        date_time=data['date_time'],
        user=user_profile,
    )

    return Response()


@api_view(['POST'])
def sleep_hours(request):
    data = request.data

    user_profile = CustomUser.objects.get(
        account=data['account'],
    )

    SleepHours.objects.create(
        num_of_sleep_hours=data['heart_rate'],
        date=data['date'],
        user=user_profile,
    )

    return Response()


@api_view(['POST'])
def calculate_calories(request):
    data = request.data

    user_profile = CustomUser.objects.get(
        account=data['account'],
    )

    return Response([user_profile.height, user_profile.weight])
