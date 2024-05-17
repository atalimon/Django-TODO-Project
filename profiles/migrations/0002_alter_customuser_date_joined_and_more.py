# Generated by Django 5.0 on 2024-04-17 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 7, 48, 46, 893902, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]