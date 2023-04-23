from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm
from .models import Academia


def home(request):
    return render(request, 'gym/pages/home.html')


def email_check(self, email):
    return Academia.E_mail.endwith("@gmail.com")


def logar(email, senha):
    login = Academia.objects.filter(E_mail=email, senha=senha).exists()
    print(login)
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
        form.save()

        messages.success(request, 'usuario cadastrado')

        del (request.session['register_form_data'])

    return redirect('gym:login')
