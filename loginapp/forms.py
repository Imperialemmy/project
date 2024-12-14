from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField( max_length = 50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length = 50)
    email = forms.EmailField()
    password = forms.CharField()


    