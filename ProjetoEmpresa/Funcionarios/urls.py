from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import PainelView

urlpatterns = [
    path('', views.home, name='home'),
    path('painel/', PainelView.as_view(), name='painel'),
    path('perfil/', views.perfil, name='perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html', next_page='painel'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]