from django.shortcuts import render

from .forms import RegisterForm


# Create your views here.
def login(request):
    return render(request, 'gym/pages/login.html')


def cadastro(request):
    form = RegisterForm()
    return render(request, 'gym/pages/cadastro.html', {
        'form': form,
    })
