from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def login(request):
    return render(request, 'login.html')

def auth_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            register_form = RegisterForm()
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('index')
        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            login_form = LoginForm()
            if register_form.is_valid():
                register_form.save()
                username = register_form.cleaned_data.get('username')
                raw_password = register_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
    else:
        login_form = LoginForm()
        register_form = RegisterForm()
    
    return render(request, 'auth.html', {'login_form': login_form, 'register_form': register_form})