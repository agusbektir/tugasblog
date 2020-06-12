from django import forms

from members.models import Member


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['photo']