# Generated by Django 5.0 on 2024-04-27 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 6, 23, 35, 62406, tzinfo=datetime.timezone.utc)),
        ),
    ]