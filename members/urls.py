from django.urls import path
from django.contrib.auth import views as auth_views
from members.views import (
    register_page,
    login_page,
    logout_page,
    dashboard_page,
    profile_page,
    home_page,
    delete_photo_profile, upload_photo_profile
)

app_name = 'members'

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('profile/<username>', profile_page, name='profile'),
    path('home', home_page, name='home'),
    path('dashboard/upload/', upload_photo_profile, name='upload_photo_profile'),
    path('dashboard/delete/', delete_photo_profile, name='delete_photo_profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
]