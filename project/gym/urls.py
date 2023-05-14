
from django.urls import path

from . import views

app_name = 'gym'
urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/create/', views.cadastro_create, name='create'),
    path('login/', views.login_view, name='login'),
    path('login/create', views.login_create, name='login_create'),
    path('login/reset_senha', views.recuperar_senha, name='recuperar_senha'),
    path('login/reset_senha_create', views.recuperar_senha_create,
         name='recuperar_senha_create'),
    path('email/', views.envia_email, name='envia_email'),
    path('login/senha/<uid64>', views.senha, name='senha'),
    path('login/senha/<uid64>/create', views.senha_create, name='senha_create'),
]
