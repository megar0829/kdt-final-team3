from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django import forms
from .models import Editor


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
    nickname = forms.CharField(
        label=False, label_suffix='',
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control signup-input',
                'placeholder': '닉네임',
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
        fields = ('username','nickname','email','password1','password2')

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(
        label=False, label_suffix='',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '성',
                }
            )
        )
    last_name = forms.CharField(
        label=False, label_suffix='',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '이름',
                }
            )
        )
    nickname = forms.CharField(
        label=False, label_suffix='',
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control signup-input',
                'placeholder': '닉네임',
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
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name', 'nickname', 'email', 'image',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['image'].widget.attrs['class']='form-control'

        
        
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
    old_password = forms.CharField(
        label=False, label_suffix='',
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '이전 비밀번호',
                }
            )
        )
    new_password1 = forms.CharField(
        label=False, label_suffix='',
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '변경 비밀번호',
                }
            )
        )
    

    new_password2 = forms.CharField(
        label=False, label_suffix='',
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control signup-input',
                'placeholder' : '비밀번호 확인',
                }
            )
        )
    class Meta(PasswordChangeForm):
        model = get_user_model()
        fields = '__all__'


class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = '__all__'