# Generated by Django 5.0 on 2024-05-08 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 4, 53, 49, 509405, tzinfo=datetime.timezone.utc)),
        ),
    ]