from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('auth/', views.auth_view, name='auth'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

]
