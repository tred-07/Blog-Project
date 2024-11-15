from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,SetPasswordForm,AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django import forms
from .models import Blog

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=(forms.TextInput(attrs={'id':'required'})))
    last_name=forms.CharField(widget=(forms.TextInput(attrs={'id':'required'})))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']



class EditForm(UserChangeForm):
      password=None
      class Meta:
           model=User
           fields=['username','first_name','last_name','email']



class BlogForm(forms.ModelForm):
     class Meta:
          model=Blog
          exclude=['author','date']
