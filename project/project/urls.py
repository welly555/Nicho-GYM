
# from django.contrib import admin
# from django.urls import path
# from gym import views

# app_name = 'gym'

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cadastro/', views.cadastro, name='cadastro'),
#     path('cadastro_confime/', views.cadastro_confirme, name='confirmar'),
#     path('login/', views.login, name='login'),

# ]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gym.urls')),

]

