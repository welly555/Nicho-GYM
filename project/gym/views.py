from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'gym/pages/login.html')

def cadastro(request):
    return render(request, 'gym/pages/cadastro.html')