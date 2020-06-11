from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from articles.models import AskMe
from members.forms import RegisterForm, LoginForm, AddPhotoForm
from members.models import Member


def register_page(request):
    form = RegisterForm(request.POST or None, use_required_attribute=False)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, email=email, password=password)
            member = Member.objects.create(user=user)

            url = reverse('members:login')
            return redirect(url)
    context = {
        'register_form':form
    }
    return render(request, 'members/register.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('members:dashboard')
        return redirect('members:login')
    context = {
        'form':form
    }
    return render(request, 'members/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('members:login')

@login_required(login_url='members:login')
def dashboard_page(request):
    if request.user.is_authenticated:
        member = request.user.member
        questions = AskMe.objects.filter(author=member)
        # photo_form = AddPhotoForm(request.POST or None, use_required_attribute=False)
        # if request.method == 'POST':
        #     if photo_form.is_valid():
        #         photo_form.save()
        context = {
            'questions':questions,
            # 'photo_form':photo_form
        }
        return render(request, 'members/dashboard.html', context)

def profile_page(request, username):
    profile = get_object_or_404(User, username=username)
    context = {
        'profile': profile,
    }
    return render(request, 'members/profile.html', context)

def home_page(request):
    return render(request, 'home.html')


