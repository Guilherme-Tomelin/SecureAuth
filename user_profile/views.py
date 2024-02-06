from django.shortcuts import render
from users.models import User
from users.forms import UserProfileForm
from django.shortcuts import redirect



def profile(request):
    return render(request, 'profile.html')


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