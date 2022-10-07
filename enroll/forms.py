from django.core import validators  
from  django import forms
#from .models import User

class StudentRegistration(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model = User
#         fields  = ['name','email','password']
#         Widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.EmailInput(attrs={'class':'form-control'}),
#             'password': forms.PasswordInput(attrs={'class':'form-control'}),
          
#         }   
