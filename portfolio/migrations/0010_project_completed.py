# Generated by Django 3.2.12 on 2022-03-18 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20220318_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 21, 36, 29, 891003)),
            preserve_default=False,
        ),
    ]
