# Generated by Django 3.0.5 on 2020-04-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20200411_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='id_on_map',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='on_map',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='xcor',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='ycor',
            field=models.FloatField(null=True),
        ),
    ]
