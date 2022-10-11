# Generated by Django 4.1.1 on 2022-10-11 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0004_rename_user_user_detail_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_detail",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]