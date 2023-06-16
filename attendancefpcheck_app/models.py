from django.db import models
from django.contrib.auth.models import User;
from django.contrib.auth.models import AbstractUser
from datetime import datetime;


# Create your models here.

class User(AbstractUser):
	pass


class Lecteur(models.Model):
    id = models.AutoField(primary_key=True);
    designation = models.CharField(max_length=100, blank=False, null=False, default=' ');
    description = models.TextField(max_length=250, blank=False, null=True, default=' ');
    num_serie = models.CharField(max_length=150, blank=False, null=True, default=' ');
    type_list = ['Optique','Capacitif','Ultrasonique', 'Thermique',];
    ALL_TYPE = sorted([(item, item) for item in type_list]);
    type_lecteur = models.CharField(
            max_length=15, 
            choices=ALL_TYPE,
            );

    class Meta:
        ordering = ['designation'];

    def __str__(self):
        return self.designation;



class Empreinte(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False);#, related_name='models', related_query_name='model');
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE, blank=False, null=False); #, related_name='models', related_query_name='model');

    type_list = ['Pouce Droit','Index Droit','Majeur Droit', 'Annulaire Droit', 'Auriculaire Droit','Pouce Gauche','Index Gauche','Majeur Gauche', 'Annulaire Gauche', 'Auriculaire Gauche', ];
    ALL_TYPE = sorted([(item, item) for item in type_list]);
    type_empreinte = models.CharField(
            max_length=20, 
            choices=ALL_TYPE,
            );
    minutie = models.CharField(max_length=250, blank=False, null=False, default=' ');
    chemin_image = models.ImageField(upload_to='photos');

    class Meta:
        ordering = ['type_empreinte'];

    def __str__(self):
        return self.type_empreinte;


class Entreprise(models.Model):
    id = models.AutoField(primary_key=True);
    raison_sociale = models.CharField(max_length=100, blank=False, null=False, default=' ');
    heure_normale_arrivee = models.TimeField(null=False, blank=False, default=datetime.now());
    heure_normale_depart = models.TimeField(null=False, blank=False, default=datetime.now());
    duree_horaire_normale = models.PositiveIntegerField(default=1, help_text='En heures');

    class Meta:
        ordering = ['raison_sociale'];

    def __str__(self):
        return self.raison_sociale;


class Presence(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False); #, related_name='models', related_query_name='model');
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, blank=False, null=False); #, related_name='models', related_query_name='model');
    date_heure_entree = models.DateTimeField(null=False, blank=False)
    date_heure_sortie = models.DateTimeField(null=False, blank=False)

    '''
    class Meta:
        ordering = ['raison_sociale'];

    def __str__(self):
        return self.raison_sociale;
    '''
    #======================

