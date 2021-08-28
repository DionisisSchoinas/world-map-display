# Generated by Django 3.0.5 on 2020-05-14 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20200514_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='color',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
