from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


def home(request):
    return render(request)

# Create your views here.


def login(request):
    return render(request, 'gym/pages/login.html')


def cadastro(request):
    register_from_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_from_data)
    return render(request, 'gym/pages/cadastro.html', {
        'form': form,
    })


def cadastro_create(request):
    # if not request.POST:
    #     raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('cadastro')
