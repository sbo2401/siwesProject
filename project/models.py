from django.db import models

# Create your models here.
class Test(models.Model):
    complaint = models.CharField(max_length=255, default="")
    details = models.TextField(default="")
