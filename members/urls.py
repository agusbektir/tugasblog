from django.urls import path
from members.views import (
    register_page,
    login_page,
    logout_page,
    dashboard_page,
    profile_page,
    home_page,
    edit_photo_profile
)

app_name = 'members'

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('profile/<username>', profile_page, name='profile'),
    path('home', home_page, name='home'),
    path('dashboard/<username>', edit_photo_profile, name='edit_photo_profile'),
]