# Generated by Django 3.2.12 on 2022-03-15 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='completed',
            field=models.DateField(default=datetime.datetime(2022, 3, 15, 12, 21, 17, 172324)),
            preserve_default=False,
        ),
    ]
