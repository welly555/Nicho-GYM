
from django.urls import path

from . import views

app_name = 'gym'
urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/create/', views.cadastro_create, name='create'),
    path('login/', views.login_view, name='login'),
    path('login/create', views.login_create, name='login_create'),

]
