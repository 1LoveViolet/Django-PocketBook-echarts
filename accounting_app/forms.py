
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserInfo, Account

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'password_confirm']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_confirm

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'password']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['title', 'time', 'type', 'account', 'remarks']
        widgets = {
            'time': forms.DateInput(format='%Y-%m-%d'),
        }
