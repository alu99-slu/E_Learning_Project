# from .models import Employee
from django import forms

class FeebbackForm(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Enter First Name'}, widget=forms.TextInput 
    (attrs={'placeholder':'Enter First Name','class':'form-control'}))

    last_name = forms.CharField(error_messages={'required':'Enter Last Name'},
    widget=forms.TextInput
    (attrs={'placeholder': 'Enter Second Name', 'class': 'form-control'}))

    email_address = forms.EmailField(error_messages={'required':'Enter Email Address'},
    widget=forms.TextInput  
    (attrs={'placeholder':'Enter Email Address', 'class': 'form-control'}))

    phone = forms.IntegerField(error_messages={'required':'Enter Phone Number'},
    widget=forms.TextInput 
    (attrs={'placeholder':'Enter Phone Number', 'class': 'form-control'}))

    message = forms.CharField(error_messages={'required':'Enter Message'},
    widget=forms.Textarea
    (attrs={'placeholder': 'Enter the message', 'class': 'form-control'}))


