# Generated by Django 3.1.7 on 2021-04-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_propic_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='vehicle',
            field=models.CharField(blank=True, choices=[('Two wheeler', 'Two wheeler'), ('Three wheeler', 'Three wheeler'), ('Four wheeler', 'Four wheeler')], default='Four wheeler', max_length=20),
        ),
    ]
