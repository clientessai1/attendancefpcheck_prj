from django.contrib import admin;
from django.contrib.auth.admin import UserAdmin;
from .models import User;
from attendancefpcheck_app.models import *;

# Register your models here.

class UserEmpreinteInline(admin.TabularInline):
    model = Empreinte;
    readonly_fields = ('id', 'image_tag', );
    extra = 1;
    pass;

class UserEmployeeInline(admin.StackedInline):
    model = Employee;
    can_delete = False;
    verbose_name_plural = "employee";
    pass;

class UserAdmin(UserAdmin):
    inlines = (UserEmployeeInline, UserEmpreinteInline, );


'''
class UserAdmin(UserAdmin):
    #list_display = ('lecteur', ) # Affiche les deux colonnes en Page Admin
    #list_display = [field.name for field in User._meta.get_fields() if not field.many_to_many] ;
    #fields = ['lecteur', ];
    pass;
'''

class LecteurAdmin(admin.ModelAdmin):
    search_fields = ('designation',) #Faire apparaître le champ de recherche 
    list_display = ('designation', 'type_lecteur','num_serie') # Affiche les deux colonnes en Page Admin
    list_filter = ('designation', 'type_lecteur','num_serie' ) # Affiche les deux colonnes en Page Admin
    #fields = ['user'];
#    inlines = (EmpreinteInline, );
    pass;

class EmpreinteAdmin(admin.ModelAdmin):
    search_fields = ('user', 'type_empreinte') #Faire apparaître le champ de recherche 
    list_display = ('user', 'type_empreinte', 'minutie', 'image_tag') # Affiche les deux colonnes en Page Admin
    list_filter = ('user', 'type_empreinte') # Affiche les deux colonnes en Page Admin
    pass;


class EntrepriseAdmin(admin.ModelAdmin):
    search_fields = ('raison_sociale',) #Faire apparaître le champ de recherche 
    list_display = ('raison_sociale', 'heure_normale_arrivee', 'heure_normale_depart','duree_horaire_normale') # Affiche les deux colonnes en Page Admin
    list_filter = ('raison_sociale', ) # Affiche un champ de filtre sur les domaines
    pass;


class AuthentificationAdmin(admin.ModelAdmin):
    #search_fields = ('entreprise', 'user',) #Faire apparaître le champ de recherche 
    search_fields = ('user','user_entreprise', ) #Faire apparaître le champ de recherche 
    #list_display = ('entreprise', 'user', 'date_heure_entree', 'date_heure_sortie',) # Affiche les deux colonnes en Page Admin
    list_display = ('user', 'type_auth', 'date', 'heure','user_entreprise', ) # Affiche les deux colonnes en Page Admin
    #list_filter = ('entreprise', 'user') # Affiche un champ de filtre sur les domaines
    list_filter = ('user',) # Affiche un champ de filtre sur les domaines
    pass;


admin.site.register(User, UserAdmin);
admin.site.register(Lecteur, LecteurAdmin);
admin.site.register(Empreinte, EmpreinteAdmin);
admin.site.register(Entreprise, EntrepriseAdmin);
admin.site.register(Authentification, AuthentificationAdmin);

