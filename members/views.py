from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

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
        form = AddPhotoForm()
        questions = AskMe.objects.filter(author=member)
        context = {
            'questions':questions,
            'form':form,
            'member':member
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

def edit_photo_profile(request, username):
    if request.user.is_authenticated:
        member = get_object_or_404(User, username=username)
        if request.method == 'POST':
            form = AddPhotoForm(request.POST, request.FILES, instance=member, use_required_attribute=False)
            if form.is_valid():
                # form.save()
                photo = form.save(commit=False)
                photo.user = request.user
                photo.save()
            return redirect('members:dashboard')
    # else:
    #     form = AddPhotoForm()
    # context = {
    #     'member':member,
    #     'form':form
    # }
    # return render(request, 'members/dashboard.html', context)
    # return redirect('members:dashboard')