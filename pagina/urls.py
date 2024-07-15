from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import productos_view, agregar_producto_view, add_to_cart, view_cart, remove_from_cart, clear_cart

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos_view, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('auth/', views.auth_view, name='auth'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('productos/agregar/', views.agregar_producto_view, name='agregar_producto'),
    path('cart/add/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)