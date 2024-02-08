from django import forms
from users.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','location', 'github', 'linkedin', 'about_me']  
