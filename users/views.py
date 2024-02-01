from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def valida_cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        # Validação dos campos de entrada
        if not username.strip() or not email.strip() or not password or not confirm_password:
            return redirect('/auth/register/?status=1')

        # Verifica se o email já está em uso
        try:
            User.objects.get(email=email)
            return redirect('/auth/register/?status=2')
        except User.DoesNotExist:
            pass

        # Verifica se as senhas correspondem
        if password != confirm_password:
            return redirect('/auth/register/?status=3')
        
        hashed_password = make_password(password)

        # Salvando
        try:
            user = User.objects.create(username=username, email=email, password=hashed_password)
            return redirect('/auth/login/?status=0')
        except ValidationError:
            return redirect('/auth/register/?status=4')
    else:
        return redirect('/auth/register/?status=5')

