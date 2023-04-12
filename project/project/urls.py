from django.contrib import admin
from django.urls import include, path
from gym import views

name = 'gym'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),

]
