# Generated by Django 2.1.5 on 2019-02-01 01:43

import django.contrib.postgres.fields
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190130_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='sharer_passenget',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=users.models.emptylist, size=None),
        ),
    ]