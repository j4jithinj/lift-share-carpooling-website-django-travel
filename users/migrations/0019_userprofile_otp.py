# Generated by Django 3.1.7 on 2021-05-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210516_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.CharField(default='no otp', max_length=20),
        ),
    ]