# Generated by Django 2.2.6 on 2020-09-15 05:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_svg'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]