from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from .models import Customer

class singUpform(UserCreationForm):
    password1 = forms.CharField(label='Password', 
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

    password2 = forms.CharField(label='Confirm Password', 
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        label = {'first_name': 'First Name','last_name': 'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter Username'}),

        'first_name':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter First Name'}),

        'last_name':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter Last Name'}),

        'email':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter Email'}),
        }


class logInform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=
    {'autofocus':True,'class':'form-control'}))

    password = forms.CharField(label=_("Password"),strip=False,
    widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))


class userEditForm(UserChangeForm):
    password=None
    
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        label = {'first_name': 'First Name','last_name': 'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter Username'}),

        'first_name':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter First Name'}),

        'last_name':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter Last Name'}),

        'email':forms.TextInput(attrs=
        {'class':'form-control','placeholder':'Enter Email'}),
        }


class UserProfileImage(forms.ModelForm):    
    class Meta:
        model = Customer
        fields = ('user_img',)
        

class changePassword(PasswordChangeForm):
   old_password = forms.CharField(label=_("Old Password"),
   strip=False, widget=forms.PasswordInput(attrs={
       'autocomplete':'current-password','autofocus':True,
       'class':'form-control'
   }))
   
   new_password1 = forms.CharField(label=("New Password"),
   strip=False, widget=forms.PasswordInput(attrs={
       'autocomplete':'new-password','class':'form-control'
   }),
   help_text=password_validation.password_validators_help_text_html())

   new_password2 = forms.CharField(label=("Confrim New Password"),
   strip=False,widget=forms.PasswordInput(attrs={
       'autocomplete':'new-password','class':'form-control'
   }))


class password_resetForm(PasswordResetForm):
    email= forms.EmailField(label=_("Email"), max_length=257,
    widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class passwod_confirm_form(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"),
    strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password")
    ,strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
