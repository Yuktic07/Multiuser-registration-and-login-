# Generated by Django 5.0.1 on 2024-01-10 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_userprofile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
    ]
