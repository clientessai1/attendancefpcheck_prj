# Generated by Django 4.2.1 on 2023-06-22 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendancefpcheck_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentification',
            name='heure',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 6, 22, 19, 55, 56, 936453), null=True),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='heure_normale_arrivee',
            field=models.TimeField(default=datetime.datetime(2023, 6, 22, 19, 55, 56, 936453)),
        ),
    ]
