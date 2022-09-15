from django.db import models
from user_profile.models import CustomUser


class Meal(models.Model):
    date_time = models.DateTimeField()
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)


class FoodType(models.Model):
    name = models.TextField()


class Food(models.Model):
    name = models.TextField()
    num_of_calories = models.IntegerField()
    food_type = models.ForeignKey(FoodType, null=True, blank=True, on_delete=models.SET_NULL)


class MealFood(models.Model):
    weight = models.IntegerField()
    meal = models.ForeignKey(Meal, null=True, blank=True, on_delete=models.SET_NULL)
    food = models.ForeignKey(Food, null=True, blank=True, on_delete=models.SET_NULL)
