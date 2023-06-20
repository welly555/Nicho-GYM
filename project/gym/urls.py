
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

    path('aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('aluno/create/', views.cadastro_aluno_create, name='aluno_cadastrado'),
    path('email/', views.envia_email, name='envia_email'),
    path('login/senha/<uid64>', views.senha, name='senha'),
    path('login/senha/<uid64>/create', views.senha_create, name='senha_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/dashboard_aluno',
         views.dashboard_aluno, name='dashboard_aluno'),

    path('dashboard/dashboard_aluno/<int:pk>/edit', views.dashboard_aluno_edit, name='dashboard_aluno_edit'),
    path('dashboard/dashboard_aluno/<int:pk>/delete', views.dashboard_aluno_delete, name='dashboard_aluno_delete'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/avaliacao', views.avaliacao, name='avaliacao'),
    path('dashboard/avaliacao/create',
         views.avaliacao_create, name='avaliacao_create'),



]
