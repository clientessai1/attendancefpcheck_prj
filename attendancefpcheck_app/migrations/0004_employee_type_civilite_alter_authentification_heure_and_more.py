# Generated by Django 4.2.1 on 2023-07-04 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendancefpcheck_app', '0003_alter_authentification_heure_alter_empreinte_minutie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='type_civilite',
            field=models.CharField(choices=[('M', 'M'), ('Mme', 'Mme')], default='M', max_length=20),
        ),
        migrations.AlterField(
            model_name='authentification',
            name='heure',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 7, 4, 3, 26, 7, 801919), null=True),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='heure_normale_arrivee',
            field=models.TimeField(default=datetime.datetime(2023, 7, 4, 3, 26, 7, 801919)),
        ),
    ]