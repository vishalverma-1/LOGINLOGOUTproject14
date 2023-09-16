# Generated by Django 4.2.3 on 2023-08-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('conform_password', models.CharField(max_length=15)),
            ],
        ),
    ]