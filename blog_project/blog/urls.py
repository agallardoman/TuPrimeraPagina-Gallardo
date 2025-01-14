from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
