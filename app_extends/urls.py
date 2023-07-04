from django.urls import path, re_path;
from . import views; #From the current directory import views.

urlpatterns = [
        path('', views.home, name='home'),
        #path('<str:message_succes>', views.home, name='home'),
        #re_path(r'^(P<message_succes>[\w+])/$', views.home, name='home'),
        path('entree', views.demandeEntree , name='demandeEntree'),
        path('sortie', views.demandeSortie , name='demandeSortie'),

        re_path(r'^message_succes=(?P<message_succes>.+)/$', views.home, name='home'),
        #re_path(r'^[\w\[\]]+', views.home, name='home'),
        #re_path(r'^<str:message_succes>[\w\[\]]+', views.home, name='home'),
        ];
