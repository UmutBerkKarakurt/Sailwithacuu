from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

# Kayıt olma (signup)
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Kullanıcıyı kaydet
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()

            return render(request, 'signup_success.html', {'name': name})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Giriş yapma (login)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'main/login_success.html', {'email': email})
                else:
                    return render(request, 'main/login.html', {'form': form, 'error': 'Geçersiz şifre.'})
            except User.DoesNotExist:
                return render(request, 'main/login.html', {'form': form, 'error': 'Bu e-posta ile kullanıcı bulunamadı.'})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})
