from django.shortcuts import render;
from django.shortcuts import redirect;
from .forms import AppExtendsForm;
import os;
import cv2;
import numpy;
from .functions_help import checkFingerPrintMatchV1;
from attendancefpcheck_app.models import Authentification, User;
#(original_img_folder, suspected_img_path):

# Create your views here
from django.shortcuts import HttpResponse;
from urllib.parse import urlencode, unquote_plus;


def home(request, message_succes=None):
    my_context = {};
    if(message_succes != None):
        my_context['message_succes'] = unquote_plus(message_succes);
    #my_context['my_form'] = AppExtendsForm();
    print(request.GET);
    print(message_succes);
    print(" + + + + + + + + + + ");
    return render(request, 'home.html', my_context);
    #return HttpResponse("<h3>Cool</h3>");

# = = = = = = 
def demandeEntree(request):
    my_context = {};
    message_succes = None;
    message_erreur = None;
    if (request.method == "POST"):
        my_form = AppExtendsForm(request.POST, request.FILES);
        if my_form.is_valid():
            #name = my_form.cleaned_data.get("name");
            fp_img_field = my_form.cleaned_data.get("fingerprint_image");
            print(type(fp_img_field));
            #Est tres long
            #print(fp_img_field.read());
            #chemin_tamp = fp_img_field.temporary_file_path();
            original_img_folder = "./media/photos";
            #sample = cv2.imread(chemin_tamp);
            #sample = cv2.imread(fp_img_field.read());

            #sample = cv2.imdecode(numpy.fromstring(request.FILES['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED);
            sample = cv2.imdecode(numpy.fromstring(fp_img_field.read(), numpy.uint8), cv2.IMREAD_UNCHANGED);
            result_check = checkFingerPrintMatchV1(original_img_folder , sample);
#            cv2.imshow("Sample", sample);
#            cv2.waitKey(0);
#            cv2.destroyAllWindows();
            

            #print(fp_img_field.temporary_file_path());
            print(fp_img_field.name);
            print(result_check);
            print("= = = = = = ");
            if (result_check == None):
                message_erreur = "Empreinte Inconnue. Veuillez reprendre.";
                #return HttpResponse("<h3 style='color:red;'>Empreinte Inconnue. Veuillez reprendre.</h3>");
            else:
                array_str = result_check['filename'].split('_');
                username = "";
                username_sup = "";
                if array_str != None:
                    if len(array_str) > 1:
                        username = array_str[0];
                        username_sup = f" M/Mme. {username} ";
                        objet_user = User.objects.get(username=username);
                        objet_auth = Authentification.objects.create(user=objet_user, type_auth ='Entree');
                        print(objet_auth);
                        print("= = = FINNNNNN= = = ");
                message_succes = "Entrée enregistrée pour le compte de {} ".format(username_sup);
                #return HttpResponse("<h3 style='color:green;'>Sortie bien enregistr&eacute;e {} </h3>".format(username_sup));
                #return HttpResponse("<h3 style='color:green;'>Pr&eacute;sence bien enregistr&eacute;e {} </h3>".format(username_sup));
            pass;

    if(message_succes != None):
        my_context['message_succes'] = message_succes;
        base_url = "/";
        url_params = {'message_succes':message_succes};
        #url_params = {my_context};
        encoded_params = urlencode(url_params);
        return redirect("{}{}".format(base_url, encoded_params));
    else:
        my_context['my_form'] = AppExtendsForm();
        if(message_erreur != None):
            my_context['message_erreur'] = message_erreur;
    return render(request, 'entree.html', my_context);
    #return HttpResponse("<h3>Cool</h3>");

'''
import os;
import cv2;


#fp_img_path = "SOCOFing\Altered\Altered-Hard\2__F_Left_index_finger_CR.BMP";
p_img_path = "SOCOFing/Altered/Altered-Hard/2__F_Left_index_finger_CR.BMP";
#fp_img_path = "SOCOFing/Altered/Altered-Hard/100__M_Left_index_finger_Obl.BMP";
sample = cv2.imread(fp_img_path);

cv2.imshow("Sample", sample);
cv2.waitKey(0);
cv2.destroyAllWindows();
'''


def demandeSortie(request):
    my_context = {};
    message_succes = None;
    message_erreur = None;
    if (request.method == "POST"):
        my_form = AppExtendsForm(request.POST, request.FILES);
        if my_form.is_valid():
            #name = my_form.cleaned_data.get("name");
            fp_img_field = my_form.cleaned_data.get("fingerprint_image");
            print(type(fp_img_field));
            #Est tres long
            #print(fp_img_field.read());
            #chemin_tamp = fp_img_field.temporary_file_path();
            original_img_folder = "./media/photos";
            #sample = cv2.imread(chemin_tamp);
            #sample = cv2.imread(fp_img_field.read());

            #sample = cv2.imdecode(numpy.fromstring(request.FILES['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED);
            sample = cv2.imdecode(numpy.fromstring(fp_img_field.read(), numpy.uint8), cv2.IMREAD_UNCHANGED);
            result_check = checkFingerPrintMatchV1(original_img_folder , sample);
#            cv2.imshow("Sample", sample);
#            cv2.waitKey(0);
#            cv2.destroyAllWindows();
            

            #print(fp_img_field.temporary_file_path());
            print(fp_img_field.name);
            print(result_check);
            print("= = = = = = ");
            if (result_check == None):
                message_erreur = "Empreinte Inconnue. Veuillez reprendre.";
                #return HttpResponse("<h3 style='color:red;'>Empreinte Inconnue. Veuillez reprendre.</h3>");
            else:
                array_str = result_check['filename'].split('_');
                username = "";
                username_sup = "";
                if array_str != None:
                    if len(array_str) > 1:
                        username = array_str[0];
                        username_sup = f" M/Mme. {username} ";
                        objet_user = User.objects.get(username=username);
                        objet_auth = Authentification.objects.create(user=objet_user, type_auth ='Sortie');
                        print(objet_auth);
                        print("= = = FINNNNNN Sortie = = = ");
                message_succes = "Sortie enregistrée pour le compte de {} ".format(username_sup);
                #return HttpResponse("<h3 style='color:green;'>Sortie bien enregistr&eacute;e {} </h3>".format(username_sup));
            pass;

    if(message_succes != None):
        my_context['message_succes'] = message_succes;
        base_url = "/";
        url_params = {'message_succes':message_succes};
        #url_params = {my_context};
        encoded_params = urlencode(url_params);
        return redirect("{}{}".format(base_url, encoded_params));
    else:
        my_context['my_form'] = AppExtendsForm();
        if(message_erreur != None):
            my_context['message_erreur'] = message_erreur;
    return render(request, 'sortie.html', my_context);
    # = = = = = = = 
    #my_context['my_form'] = AppExtendsForm();
    #return render(request, 'sortie.html', my_context);
    #return HttpResponse("<h3>Cool</h3>");

