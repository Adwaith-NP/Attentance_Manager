# Generated by Django 4.2.4 on 2023-12-09 17:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Manegar", "0005_rename_teacher_id_subjectdata_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subjectdata",
            old_name="username",
            new_name="user",
        ),
    ]
