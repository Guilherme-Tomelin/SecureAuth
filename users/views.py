from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from hashlib import sha256
from .forms import UserProfileForm


def home(request):
    if request.session.get('user'):  
        return render(request, 'profile.html')
    else:
        return redirect('/auth/login/')


def login(request):
    if request.session.get('user'):
        return redirect('/profile/userprofile')
    status = request.GET.get('status')
    status_message = ''
    if status == '1':
        status_message = 'Usuário não encontrado.'
    elif status == '2':
        status_message = 'Senha incorreta.'
    return render(request, 'login.html', {'status': status, 'status_message': status_message})

def register(request):
    status = request.GET.get('status')
    status_message = ''

    if status == '1':
        status_message = 'Todos os campos devem ser preenchidos.'
    elif status == '2':
        status_message = 'Senha incorreta.'
    elif status == '3':
        status_message = 'As senhas não correspondem'
    


    return render(request, 'register.html', {'status': status, 'status_message': status_message})


def logout(request):
    request.session.flush()
    return redirect ('login')


def valida_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('recebimento post')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user'] = user.id
                print('User autenticado')
                print(user)
                return redirect('/profile/userprofile/')
            else:
                print('senha incorreta')
                return redirect('/auth/login/?status=2')  # Senha incorreta
        except User.DoesNotExist:
            print('User nao encontrado')
            return redirect('/auth/login/?status=1')  # Usuário não encontrado

    elif request.method == 'GET':
        print('Método não permitido')
        return HttpResponse("Método não permitido")




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
            print('status 2......')
            return redirect('/auth/register/?status=2')
        except User.DoesNotExist:
            pass

        # Verifica se as passwords correspondem
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



def handler404(request, exception):
    return render(request, '404.html')