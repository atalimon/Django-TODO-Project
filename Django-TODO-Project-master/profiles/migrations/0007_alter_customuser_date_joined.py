# Generated by Django 5.0 on 2024-04-28 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 28, 7, 27, 46, 568159, tzinfo=datetime.timezone.utc)),
        ),
    ]
