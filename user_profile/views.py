from django.shortcuts import render
from users.models import User
from users.forms import UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def profile(request):
    if request.session.get('user'):  
        return render(request, 'profile.html')
    else:
        return redirect('/auth/login/?status=2')


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile/edit_profile/')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})
