from django import forms 
class AppExtendsForm(forms.Form):
#    name = forms.CharField();
    fingerprint_image = forms.ImageField();
