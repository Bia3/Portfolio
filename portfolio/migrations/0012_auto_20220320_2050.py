# Generated by Django 3.2.12 on 2022-03-20 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20220320_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculumvitae',
            options={'verbose_name_plural': 'CVs'},
        ),
        migrations.AlterModelOptions(
            name='responsibility',
            options={'verbose_name_plural': 'Responsibilities'},
        ),
        migrations.AddField(
            model_name='responsibility',
            name='started',
            field=models.DateField(default=datetime.date(2022, 3, 20)),
        ),
    ]