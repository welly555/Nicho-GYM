from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


def home(request):
    return render(request)


def login(request):
    return render(request, 'gym/pages/login.html')


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

        del(request.session['register_form_data'])
        
    return redirect('gym:cadastro')
