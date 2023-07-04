from django.db import models
from django.contrib.auth.models import User;
from django.contrib.auth.models import AbstractUser
from datetime import datetime;
from datetime import date;
from django.utils.safestring import mark_safe;


# Create your models here.

class User(AbstractUser):
    pass;

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
    user = models.ManyToManyField(User, through='Empreinte');
    

    class Meta:
        ordering = ['designation'];

    def __str__(self):
        return self.designation;


'''
class User(AbstractUser):
    lecteur = models.ManyToManyField(Lecteur, through='Empreinte');
    pass;
'''

def upload_location(instance, filename):
    filebase, extension = filename.split('.');
    new_composed_name = f"{instance.user.username}_{instance.type_empreinte}";
    return 'photos/%s.%s' % (new_composed_name, extension);

class Empreinte(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False);#, related_name='models', related_query_name='model');
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE, blank=False, null=False); #, related_name='models', related_query_name='model');

    type_list = ['Droit-Pouce','Droit-Index','Droit-Majeur', 'Droit-Annulaire', 'Droit-Auriculaire','Gauche-Pouce','Gauche-Index','Gauche-Majeur', 'Gauche-Annulaire', 'Gauche-Auriculaire', ];
    ALL_TYPE = sorted([(item, item) for item in type_list]);
    type_empreinte = models.CharField(
            max_length=20, 
            choices=ALL_TYPE,
            );
    minutie = models.CharField(max_length=250, blank=True, null=True, default='');
    chemin_image = models.ImageField(upload_to=upload_location);
    #chemin_image = models.ImageField(upload_to='photos');

    def image_tag(self):
        if self.chemin_image.url is not None:
            return mark_safe('<img src="{}" height="50" />'.format(self.chemin_image.url));
        else:
            return "";
            pass;
        pass;

    class Meta:
        ordering = ['type_empreinte'];

    def __str__(self):
        return self.type_empreinte;


class Entreprise(models.Model):
    id = models.AutoField(primary_key=True);
    raison_sociale = models.CharField(max_length=100, blank=False, null=False, default=' ');
    heure_normale_arrivee = models.TimeField(null=False, blank=False, default=datetime.now());
    heure_normale_depart = models.TimeField(null=False, blank=False, default=date.today);
    duree_horaire_normale = models.PositiveIntegerField(default=1, help_text='En heures');

    class Meta:
        ordering = ['raison_sociale'];

    def __str__(self):
        return self.raison_sociale;

class Employee(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.OneToOneField(User, on_delete=models.CASCADE);
    nom = models.CharField(max_length=250, blank=False, null=False, default='');
    prenoms = models.CharField(max_length=250, blank=False, null=False, default='');
    type_list = ['M','Mme',];
    ALL_TYPE = sorted([(item, item) for item in type_list]);
    type_civilite= models.CharField(
            #default='M',
            max_length=20, 
            choices=ALL_TYPE,
            );
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, blank=False, null=False);
    pass;

#class Presence(models.Model):
class Authentification(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False); #, related_name='models', related_query_name='model');
    #entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, blank=False, null=False); #, related_name='models', related_query_name='model');
    date = models.DateField(null=True, blank=True, default=date.today);
    heure = models.TimeField(null=True, blank=True, default=datetime.now());

    def user_entreprise(self): #callable field
        return self.user.employee.entreprise;
        pass;

    type_list = ['Entree','Sortie'];
    ALL_TYPE = sorted([(item, item) for item in type_list]);
    type_auth = models.CharField(
            max_length=10, 
            choices=ALL_TYPE,
            );

    '''
    class Meta:
        ordering = ['raison_sociale'];

    def __str__(self):
        return self.raison_sociale;
    '''
    #======================

