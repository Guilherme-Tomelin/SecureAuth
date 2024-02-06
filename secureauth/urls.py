from django.contrib import admin
from django.urls import path, include 
from user_profile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('profile/', include('user_profile.urls')),
    path('', views.profile, name='profile'),

]

handler404 = 'users.views.handler404'