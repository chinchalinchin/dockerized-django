# Generated by Django 3.2.5 on 2021-08-07 17:55

from django.db import migrations
from defaults.admin import create_superuser


class Migration(migrations.Migration):

    dependencies = [
        ('defaults', '0001_groups'),

    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
