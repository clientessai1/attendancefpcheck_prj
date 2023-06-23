"""
URL configuration for attendancefpcheck_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin;
from django.urls import path, include;
from django.conf import settings; #New
from django.conf.urls.static import static; #New

admin.site.site_header = "Attendance FP Check"	  # Texte de Personnalisé num 1
admin.site.site_title = "Attendance FP Check Portal" # Texte de Personnalisé num 2
admin.site.index_title = "Check Attendance by FingerPrint" # Texte de Personnalisé num 3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_extends.urls')),
]
if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
