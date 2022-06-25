from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    sir_name = forms.CharField(max_length=100)
    email = forms.EmailField()


class LoginForm(forms.Form):
    email = forms.EmailField()
