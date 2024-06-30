from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from .forms import ProductoForm
from .forms import AddToCartForm
from .models import Producto, Cart, CartItem
from django.contrib.auth.decorators import login_required

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


@login_required
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


@login_required
def add_to_cart(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, producto=producto)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f'Added {quantity} x {producto.nombre} to your cart.')
            return redirect('productos')
    else:
        form = AddToCartForm()

    return render(request, 'add_to_cart.html', {'form': form, 'producto': producto})

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    
    total = sum(item.producto.precio * item.quantity for item in items)
    
    return render(request, 'view_cart.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('view_cart')

@login_required
def clear_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    CartItem.objects.filter(cart=cart).delete()
    messages.success(request, 'All items removed from cart.')
    return redirect('view_cart')