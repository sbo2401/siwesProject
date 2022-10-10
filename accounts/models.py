from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.
class Userdetail(models.Model):
    first_name = models.CharField(max_length=255, default="")
    middle_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    country = CountryField()
    email = models.EmailField(max_length=255, default="")
    date_of_birth = models.DateTimeField(null=False, blank=False, default="")
    tel = PhoneNumberField()
