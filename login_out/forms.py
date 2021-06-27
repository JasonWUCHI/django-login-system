from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class loginForm(forms.Form):
    username = forms.CharField()  #the email
    password = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact = username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid username")
        return username

class registerForm(forms.Form):
    last_name = forms.CharField()
    first_name = forms.CharField()
    prefer_name = forms.CharField()
    gender = forms.CharField()
    school = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact = email)
        if qs.exists():
            raise forms.ValidationError("This email is used")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirms_password')
        if(password != confirm_password):
            raise forms.ValidationError("Inconsistent Password")
        return password
