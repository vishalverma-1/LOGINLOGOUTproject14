# Generated by Django 4.2.3 on 2023-08-29 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='conform_password',
        ),
    ]
