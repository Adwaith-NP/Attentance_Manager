# Generated by Django 4.2.1 on 2023-12-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Manegar", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjectdata",
            name="subjectCode",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
