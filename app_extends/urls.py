from django.urls import path;
from . import views; #From the current directory import views.

urlpatterns = [
        path('', views.home, name='home'),
        path('sortie', views.demandeSortie , name='demandeSortie'),
        ];
