# Generated by Django 4.2.4 on 2023-12-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logindata",
            name="is_student",
            field=models.BooleanField(default=True),
        ),
    ]
