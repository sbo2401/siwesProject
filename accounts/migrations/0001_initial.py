# Generated by Django 4.1.1 on 2022-10-11 00:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User_detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(default="", max_length=255)),
                ("last_name", models.CharField(default="", max_length=255)),
                ("email", models.EmailField(default="", max_length=255)),
                ("date_of_birth", models.DateField(default="")),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHERS", "Prefer not to say"),
                        ],
                        default="",
                        max_length=50,
                    ),
                ),
                (
                    "tel",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
            ],
        ),
    ]
