# Generated by Django 5.0 on 2024-04-28 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 28, 7, 29, 25, 513116, tzinfo=datetime.timezone.utc)),
        ),
    ]
