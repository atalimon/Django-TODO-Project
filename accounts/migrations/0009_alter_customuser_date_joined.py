# Generated by Django 5.0 on 2024-01-01 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 6, 18, 8, 193719, tzinfo=datetime.timezone.utc)),
        ),
    ]
