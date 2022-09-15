from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_profile.models import CustomUser
from .models import MedicalExaminationsType, MedicalExaminationsRecords


@api_view(['POST'])
def build_examinations_record(request):
    data = request.data

    user_profile = CustomUser.objects.get(
        account=data['account'],
    )

    date_time = f"{data['date']} {data['time'].split(' ')[1]}"

    try:
        lab_name = data['lab_name']
    except:
        lab_name = 'home'

    medical_examinations_type, create = MedicalExaminationsType.objects.get_or_create(name=data['medical_examinations_type'])
    MedicalExaminationsRecords.objects.create(
        measurement=data['measurement'],
        date_time=date_time,
        lab_name=lab_name,
        medical_examinationsType=medical_examinations_type,
        user=user_profile,
    )

    return Response()

# {
#         "medical_examinations_type":"glucose",
#         "measurement": 140,
#         "date_time":"2006-10-25 14:30:59",
# }
