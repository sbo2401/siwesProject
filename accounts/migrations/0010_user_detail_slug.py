# Generated by Django 4.1.1 on 2022-10-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_remove_user_detail_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_detail",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
