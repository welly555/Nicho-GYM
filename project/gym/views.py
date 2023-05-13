from django.conf import Settings, settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from .forms import LoginForm, Recuperar_senha, RegisterForm, Valid_Email
from .models import Academia


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
    messages.success(request, 'usuario cadastrado')
    register_from_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_from_data)

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
            email=request.POST.get('E_mail')
        )
        if valido:
            html_content = render_to_string(
                'gym/pages/email.html', {'nome': 'aqui vai ta o link'})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                'alterar senha', text_content, settings.EMAIL_HOST_USER, [request.POST.get('E_mail')])
            email.attach_alternative(html_content, 'text/html')
            email.send()

            return redirect('gym:login')
        else:
            messages.error(request, 'Usuario não encontrado')
            return redirect('gym:recuperar_senha')
    return redirect('gym:recuperar_senha')


def senha(request):
    register_from_data = request.session.get('register_form_data', None)
    form = Recuperar_senha(register_from_data)
    return render(request, 'gym/pages/recuperar_senha.html', context={
        'form': form,
    })


def enviar_redifinicao_senha_email(request):
    if request.method == 'POST':
        form = Recuperar_senha(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('email')


def envia_email(request,):
    html_content = render_to_string(
        'gym/pages/email.html', {'nome': 'aqui vai ta o link'})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        'alterar senha', text_content, settings.EMAIL_HOST_USER, ['wellyngton.targino@aluno.uepb.edu.br'])
    email.attach_alternative(html_content, 'text/html')
    email.send()
    # send_mail(
    #     'Assunto',
    #     'Teste de envio de email',
    #     'wellyngtontargino10@gmail.com',
    #     ['wellyngton.targino@aluno.uepb.edu.br']
    # )
    return HttpResponse('OLá')
