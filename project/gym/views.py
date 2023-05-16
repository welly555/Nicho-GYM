from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import check_password, make_password
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, Recuperar_senha, RegisterForm
from .forms.aluno import AlunoRegister
from .models import Academia, Aluno


def home(request):
    return render(request, 'gym/pages/home.html')


def check_email(email):
    check = Academia.objects.filter(E_mail=email).exists()
    if check:
        return True
    return False


def atualizar_senha(email, senha):
    user = Academia.objects.filter(E_mail=email).first()
    user.senha = senha
    user.save()


def logar(email, senha):
    login = Academia.objects.filter(E_mail=email, senha=senha).exists()

    if login:
        return True
    return False


def login_view(request):
    form = LoginForm()
    return render(request, 'gym/pages/login.html', {
        'form': form,
        'form_action': reverse('gym:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    if form.is_valid():
        valido = logar(
            email=request.POST.get('E_mail'),
            senha=request.POST.get('Senha')
        )
        if valido:
            messages.success(request, 'login efetuado')

            return redirect('gym:home')
        else:
            messages.error(request, 'credeciais erradas')
            return redirect('gym:login')
    else:
        messages.error(request, 'usuario inexistente')
        return redirect('gym:login')


def cadastro(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'gym/pages/cadastro.html', {
        'form': form,
    })


def cadastro_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():

        form.save(commit=False)
        form.save()
        messages.success(request, 'usuario cadastrado')

        del (request.session['register_form_data'])
        return redirect('gym:login')

    return redirect('gym:cadastro')


def recuperar_senha(request):
    register_form_data = request.session.get('register_form_data', None)
    form = Recuperar_senha(register_form_data)
    return render(request, 'gym/pages/recuperar_senha.html', {
        'form': form
    })


def recuperar_senha_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = Recuperar_senha(POST)
    if form.is_valid():
        valido = check_email(
            email=request.POST.get('E_mail')
        )
        if valido:
            atualizar_senha(
                email=request.POST.get('E_mail'),
                senha=request.POST.get('Senha')
            )
            messages.success(request, 'Senha atualizada com sucesso')
            return redirect('gym:login')
        else:
            messages.error(request, 'Usuario não encontrado')
            return redirect('gym:recuperar_senha')
    return redirect('gym:recuperar_senha')


@login_required(login_url='gym:login', redirect_field_name='next')
def cadastro_aluno(request):
    register_form_data = request.session.get('register_form_data', None)
    form = AlunoRegister(register_form_data)

    return render(request, 'gym/pages/aluno.html', {
        'form' : form,
    })

@login_required(login_url='gym:login', redirect_field_name='next')
# def cadastro_aluno_create(request, id):
def cadastro_aluno_create(request):
    # aluno = Aluno.objects.filter(
    #     academia=request.academia,
    #     pk=id,
    # )
    
    
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = AlunoRegister(POST)

    if form.is_valid():
        form.save()

    del (request.session['register_form_data'])

    return redirect('gym:cadastro_aluno')
