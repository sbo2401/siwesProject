# Generated by Django 4.1.1 on 2022-10-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_rename_user_detail_userdetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdetail",
            name="about_you",
            field=models.TextField(default="", max_length=255),
        ),
    ]
