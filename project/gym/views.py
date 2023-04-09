from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'gym/login.html')

def cadastro(request):
    return render(request, 'gym/cadastro.html')