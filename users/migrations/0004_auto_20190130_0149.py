# Generated by Django 2.1.5 on 2019-01-30 01:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_ride'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='users',
        ),
        migrations.AddField(
            model_name='ride',
            name='driver_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='ride',
            name='rider_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='ride',
            name='sharer_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='ride',
            name='special',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='special',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]