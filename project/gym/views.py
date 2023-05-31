import datetime
from django.conf import Settings, settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import (PasswordResetTokenGenerator,
                                        default_token_generator)
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import BadHeaderError, Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import LoginForm, Recuperar_senha, RegisterForm, Valid_Email
from .forms.aluno import AlunoRegister
from .models import Academia, Aluno


def home(request):
    return render(request, 'gym/pages/home.html')


def check_email(email):
    check = Academia.objects.filter(email=email).exists()
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
    if messages.get_messages(request):
        messages.success(request, 'Cadastro realizado com sucesso!')

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
        valido = authenticate(
            username=request.POST.get('Responsavel'),
            password=request.POST.get('Senha')
        )

        if valido is not None:
            messages.success(request, 'login efetuado')
            login(request, valido)
            return redirect('gym:dashboard')
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

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        messages.success(request, 'usuario cadastrado')

        del (request.session['register_form_data'])

        return redirect('gym:login')

    return redirect('gym:cadastro')


def recuperar_senha(request):
    register_from_data = request.session.get('register_form_data', None)

    form = Valid_Email(register_from_data)
    return render(request, 'gym/pages/valid_email.html', {

        'form': form
    })


def recuperar_senha_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = Valid_Email(POST)

    if form.is_valid():
        valido = check_email(
            email=request.POST.get('email')
        )
        if valido:

            user = Academia.objects.filter(
                email=request.POST.get('email')).first()
            # token_genetator = PasswordResetTokenGenerator()
            # token = token_genetator.make_token(user)
            c = {
                'email': user.email,
                'domain': request.META['HTTP_HOST'],
                'site_name': 'Nicho GYM',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'id': user.pk,
                'user': user,
                # 'token': token,
                'protocol': 'https' if request.is_secure() else 'http'
            }
            html_content = render_to_string(
                'gym/pages/email.html', c)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                'alterar senha', text_content, settings.EMAIL_HOST_USER, [request.POST.get('email')])
            email.attach_alternative(html_content, 'text/html')
            email.send()

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
        'form': form,
    })


@login_required(login_url='gym:login', redirect_field_name='next')
def cadastro_aluno_create(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = AlunoRegister(POST)

    # if form.Data_pagamento == None:
    #     form.Data_pagamento = datetime.date.today() + datetime.timedelta(days=30)
    
    if form.is_valid():

        aluno = form.save(commit=False)
        aluno.academia = request.user
        aluno.save()
        messages.success(request, 'aluno adicionado')
    else:
        messages.error(request, 'aluno não adicionado')
        return redirect('gym:cadastro_aluno')

    del (request.session['register_form_data'])

    return redirect('gym:dashboard_aluno')


def senha(request, uid64):
    register_from_data = request.session.get('register_form_data', None)
    form = Recuperar_senha(register_from_data)
    return render(request, 'gym/pages/recuperar_senha.html', context={
        'form': form,
        'uid': uid64
    })


def senha_create(request, uid64):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = Recuperar_senha(POST)
    if form.is_valid():
        user = Academia.objects.filter(pk=urlsafe_base64_decode(uid64)).first()

        user.password = request.POST.get('Senha')
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Senha atualizada com sucesso')
        return redirect('gym:login')
    else:
        messages.error(request, 'Não foi possivel atualizar a senha')
        return redirect('gym:home')


def envia_email(request,):
    html_content = render_to_string(
        'gym/pages/email.html', {'nome': 'aqui vai ta o link'})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        'alterar senha', text_content, settings.EMAIL_HOST_USER, ['wellyngton.targino@aluno.uepb.edu.br'])
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return HttpResponse('OLá')


@login_required(login_url='gym:login', redirect_field_name='next')
def dashboard(request):
    quantidade_alunos = Aluno.objects.filter(
        academia = request.user
    ).count()
    quantidade_pendente = Aluno.objects.filter(
        Situacao=False,
        academia = request.user
    ).count()
    return render(request,'gym/pages/dashboard.html', context={
        'quantidade_alunos': quantidade_alunos,
        'quantidade_pendente' : quantidade_pendente
    })


@login_required(login_url='gym:login', redirect_field_name='next')
def dashboard_aluno(request):
    alunos = Aluno.objects.filter(
        academia = request.user
    )
    return render(
        request, 
        'gym/pages/dashboard_aluno.html',
        {
            'alunos' : alunos,
        }
    )


@login_required(login_url='gym:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('gym:login'))

    if request.POST.get('username') != request.user.username:
        print('você caiu aqui')
        return redirect(reverse('gym:login'))
    logout(request)
    return redirect(reverse('gym:login'))
