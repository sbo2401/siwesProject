from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.
GENDER = (
    ("MALE", 'Male'),
    ("FEMALE", 'Female'),
    ("OTHERS", "Prefer not to say"),
)
class User_detail(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    other_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    date_of_birth = models.DateField(null=False, blank=False, default="")
    gender = models.CharField(max_length=50, choices=GENDER, default="")
    tel = PhoneNumberField()
