# Generated by Django 5.0.6 on 2024-06-04 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 12, 49, 9, 470288, tzinfo=datetime.timezone.utc)),
        ),
    ]
