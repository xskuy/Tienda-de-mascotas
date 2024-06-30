from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos_view, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('auth/', views.auth_view, name='auth'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('productos/agregar/', views.agregar_producto_view, name='agregar_producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)