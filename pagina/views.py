from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from .forms import ProductoForm
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def auth_view(request):
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Error en el inicio de sesión. Por favor, verifica tus credenciales.')
        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, 'Registro exitoso. Bienvenido!')
                return redirect('index')
            else:
                print(register_form.errors)  # Imprimir errores del formulario en la consola
                messages.error(request, 'Error en el registro. Por favor, corrige los errores.')

    return render(request, 'auth.html', {'login_form': login_form, 'register_form': register_form})


def cart_view(request):
    # Lógica para el carrito de compras
    return render(request, 'cart.html')


def agregar_producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})


def productos_view(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})
    