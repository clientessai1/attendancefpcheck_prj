from django.contrib import admin;
from django.contrib.auth.admin import UserAdmin;
from .models import User;
from attendancefpcheck_app.models import *;

# Register your models here.


class LecteurAdmin(admin.ModelAdmin):
    search_fields = ('designation',) #Faire apparaître le champ de recherche 
    list_display = ('designation', 'type_lecteur','num_serie') # Affiche les deux colonnes en Page Admin
    list_filter = ('designation', 'type_lecteur','num_serie' ) # Affiche les deux colonnes en Page Admin
    pass;

class EmpreinteAdmin(admin.ModelAdmin):
    search_fields = ('user', 'type_empreinte') #Faire apparaître le champ de recherche 
    list_display = ('user', 'type_empreinte', 'minutie') # Affiche les deux colonnes en Page Admin
    list_filter = ('user', 'type_empreinte') # Affiche les deux colonnes en Page Admin
    pass;


class EntrepriseAdmin(admin.ModelAdmin):
    search_fields = ('raison_sociale',) #Faire apparaître le champ de recherche 
    list_display = ('raison_sociale', 'heure_normale_arrivee', 'heure_normale_depart','duree_horaire_normale') # Affiche les deux colonnes en Page Admin
    list_filter = ('raison_sociale', ) # Affiche un champ de filtre sur les domaines
    pass;


class PresenceAdmin(admin.ModelAdmin):
    search_fields = ('entreprise', 'user',) #Faire apparaître le champ de recherche 
    list_display = ('entreprise', 'user', 'date_heure_entree', 'date_heure_sortie',) # Affiche les deux colonnes en Page Admin
    list_filter = ('entreprise', 'user') # Affiche un champ de filtre sur les domaines
    pass;


admin.site.register(User, UserAdmin);
admin.site.register(Lecteur, LecteurAdmin);
admin.site.register(Empreinte, EmpreinteAdmin);
admin.site.register(Entreprise, EntrepriseAdmin);
admin.site.register(Presence, PresenceAdmin);

