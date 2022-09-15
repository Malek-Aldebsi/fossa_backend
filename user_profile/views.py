from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Pet, PetKind


@api_view(['POST'])
def check_user(request):
    data = request.data
    try:
        CustomUser.objects.get(
            account=data['account']
        )
        return Response(True)
    except:
        return Response(False)


@api_view(['POST'])
def build_profile(request):
    data = request.data

    user_profile = CustomUser.objects.create(
        account=data['account'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        date_of_birth=data['date_of_birth'],
        sex=data['sex'],
        height=data['height'],
        weight=data['weight'],
        ideal_weight=data['ideal_weight'],
        in_relationship=data['in_relationship'],
        number_of_household=data['number_of_household'],
        # image=data['image'],
    )
    user_profile.save()

    for i in range(int(data['number_of_pets'])):
        pet_kind, create = PetKind.objects.get_or_create(name=data['pet_kind'])

        Pet.objects.create(
            name=data['pet_name'],
            user=user_profile,
            pet_kind=pet_kind
        )

    return Response()

# {
#         "account":"+962786636678",
#         "first_name":"malek",
#         "last_name":"aldebsi",
#         "date_of_birth":"2002-01-23",
#         "sex":"male",
#         "height":"172.0",
#         "weight":"52.0",
#         "ideal_weight":"60.0",
#         "in_relationship":"Single",
#         "number_of_household":"8",
#         "number_of_pets":1,
#         "pet_kind":"dog",
#         "pet_name":"rex"
# }
