from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from .forms import ProductoForm
from .forms import AddToCartForm
from .models import Producto, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
def index(request):
    productos = Producto.objects.all().order_by('-id')[:4]
    context = {
        'productos': productos
    }
    return render(request, 'index.html', context)

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


def add_to_cart(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, producto=producto)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{producto.nombre} ha sido agregado al carrito.')
    return redirect('view_cart')


def view_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    items = CartItem.objects.filter(cart=cart)
    total = items.aggregate(total=Sum('producto__precio'))['total'] or 0

    context = {
        'items': items,
        'total': total
    }
    return render(request, 'view_cart.html', context)

def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_item = get_object_or_404(CartItem, id=item_id, cart__session_key=session_key)
    
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('view_cart')


def clear_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    
    CartItem.objects.filter(cart=cart).delete()
    messages.success(request, 'All items removed from cart.')
    return redirect('view_cart')