# Generated by Django 4.1.1 on 2022-10-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_userdetail_country"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdetail",
            name="country",
        ),
        migrations.AlterField(
            model_name="userdetail",
            name="date_of_birth",
            field=models.DateField(default=""),
        ),
    ]
