
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/create/', views.cadastro_create, name='create'),
    # path('login/', views.login, name='login'),

]
