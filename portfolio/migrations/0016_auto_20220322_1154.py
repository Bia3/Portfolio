# Generated by Django 3.2.12 on 2022-03-22 11:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20220320_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='responsibility',
            name='started',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 11, 54, 17, 773153, tzinfo=utc)),
        ),
    ]
