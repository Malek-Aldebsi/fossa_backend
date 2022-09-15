from django.db import models


class CustomUser(models.Model):
    sex_type = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    relationship_options = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    )

    account = models.CharField(unique=True, max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=200, choices=sex_type, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ideal_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    in_relationship = models.CharField(max_length=200, choices=relationship_options, null=True, blank=True)
    number_of_household = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)  # TODO:check

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'


class PetKind(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.TextField()
    user = models.ForeignKey(CustomUser, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)
    pet_kind = models.ForeignKey(PetKind, db_constraint=False, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
