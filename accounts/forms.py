from django import forms


class Signin(forms.Form): 
    user_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control me-2 mb-4','PlaceHolder':'User Name'}))
    user_password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control me-2 mb-4','PlaceHolder':'User Password'}))
     
    
