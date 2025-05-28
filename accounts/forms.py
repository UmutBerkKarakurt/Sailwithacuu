from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100, label='Adınız')
    email = forms.EmailField(label='E-posta')
    password = forms.CharField(widget=forms.PasswordInput, label='Şifre')

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-posta')
    password = forms.CharField(widget=forms.PasswordInput, label='Şifre')
