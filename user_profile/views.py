from django.shortcuts import render
from users.models import User
from users.forms import UserProfileForm
from django.shortcuts import redirect

def profile(request):
    if request.session.get('user'):  
        user_id = request.session['user']

        try:
            user = User.objects.get(pk=user_id)
            context = {
                'username': user.username,
                'email': user.email,
                'location': user.location,
                'github': user.github,
                'linkedin': user.linkedin,
                'about_me': user.about_me
            }
            return render(request, 'profile.html', context)
        except User.DoesNotExist:
            print("sessão inválida, redirect para o login")
            return redirect('/auth/login/?status=2')
    else:
        print("sessão do usuário não contém o ID do usuário, redirect para o login")
        return redirect('/auth/login/?status=2')


def edit_profile(request):
    user_id = request.session.get('user')
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            if request.method == 'POST':
                form = UserProfileForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()
                    return redirect('/profile/userprofile/')  # Redirecione de volta para a página de perfil após a edição
            else:
                form = UserProfileForm(instance=user)
            return render(request, 'edit_profile.html', {'form': form, 'user': user})
        except User.DoesNotExist:
            # Se o usuário não existir no banco de dados (sessão inválida), redirecione para o login
            print("Sessão inválida, redirecionando para o login")
    else:
        # Se a sessão do usuário não contiver o ID do usuário, redirecione para o login
        print("A sessão do usuário não contém o ID do usuário, redirecionando para o login")
    return redirect('/auth/login/?status=2')