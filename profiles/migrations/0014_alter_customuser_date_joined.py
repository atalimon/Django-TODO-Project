# Generated by Django 5.0.6 on 2024-06-04 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 12, 47, 22, 538989, tzinfo=datetime.timezone.utc)),
        ),
    ]
