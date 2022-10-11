# Generated by Django 4.1.1 on 2022-10-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_user_detail_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_detail",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MALE", "Male"),
                    ("FEMALE", "Female"),
                    ("OTHERS", "Prefer not to say"),
                ],
                default="",
                max_length=50,
                null=True,
            ),
        ),
    ]
