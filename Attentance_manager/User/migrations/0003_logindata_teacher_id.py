# Generated by Django 4.2.4 on 2023-12-08 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0002_alter_logindata_is_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="logindata",
            name="teacher_id",
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
