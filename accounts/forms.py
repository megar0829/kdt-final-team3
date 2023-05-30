from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=False, label_suffix='',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '아이디',
                }
            )
        )
    email = forms.CharField(
        label=False, label_suffix='',
        widget=forms.EmailInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '이메일',
                }
            )
        )
    password1 = forms.CharField(
        label=False, label_suffix='',
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '비밀번호',
                }
            )
        )
    

    password2 = forms.CharField(
        label=False, label_suffix='',
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '비밀번호 확인',
                }
            )
        )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','password1','password2', )


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'
        
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=False, label_suffix='',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control login-input',
                'placeholder' : '아이디',
                }
            )
        )
    password = forms.CharField(
        label=False, label_suffix='',
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control login-input',
                'placeholder' : '비밀번호',
                }
            )
        )
    class Meta:
        medel = get_user_model()
        fields = ('username', 'password')
        


class CustomPasswordChangeForm(PasswordChangeForm):
    
    class Meta(PasswordChangeForm):
        model = get_user_model()
        fields = '__all__'


label_suffix='',