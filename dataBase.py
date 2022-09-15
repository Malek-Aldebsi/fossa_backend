# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Interest(models.Model):
#     name = models.TextField(null=True, blank=True)
#
#
# class CustomUser(models.Model):
#     sex_type = (
#         ('male', 'male'),
#         ('female', 'female'),
#     )
#
#     relationship_options = (
#         ('Single', 'Single'),
#         ('Married', 'Married'),
#         ('Widowed', 'Widowed'),
#         ('Divorced', 'Divorced'),
#     )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     sex = models.CharField(max_length=200, choices=sex_type, null=True, blank=True)
#     height = models.DecimalField(null=True, blank=True)
#     weight = models.DecimalField(null=True, blank=True)
#     ideal_weight = models.DecimalField(null=True, blank=True)
#     in_relationship = models.CharField(max_length=200, choices=relationship_options, null=True, blank=True)
#     number_of_household = models.IntegerField(null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)  # TODO:check
#     interests = models.ManyToManyField(Interest, on_delete=models.CASCADE, null=True, blank=True)
#
#
# class PetKind(models.Model):
#     name = models.TextField(null=True, blank=True)
#
#
# class Pet(models.Model):
#     name = models.TextField()
#     user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
#     pet_kind = models.ForeignKey(PetKind, null=True, blank=True, on_delete=models.SET_NULL)
#
#
# class StepsRecords(models.Model):
#     date = models.DateField()
#     numOfSteps = models.IntegerField()
#     userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
#
#
# class Meal(models.Model):
#     dateTime = models.DateTimeField()
#     userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
#
#
# class FoodType(models.Model):
#     name = models.TextField()
#
#
# class Food(models.Model):
#     name = models.TextField()
#     numOfCalories = models.IntegerField()
#     foodTypeID = models.ForeignKey(FoodType, null=True, blank=True, on_delete=models.SET_NULL)
#
#
# class MealFood(models.Model):
#     weight = models.IntegerField()
#     mealID = models.ForeignKey(Meal, null=True, blank=True, on_delete=models.SET_NULL)
#     foodID = models.ForeignKey(Food, null=True, blank=True, on_delete=models.SET_NULL)
#
#
# class MedicalExaminationsType(models.Model):
#     name = models.TextField()
#
#
# class MedicalExaminationsRecords(models.Model):
#     measurement = models.IntegerField()
#     dateTime = models.DateTimeField()
#     medicalExaminationsType = models.ForeignKey(MedicalExaminationsType, null=True, blank=True, on_delete=models.SET_NULL)
#     userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
