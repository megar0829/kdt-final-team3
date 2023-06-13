from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib import messages
from .models import User, Editor
from posts.views import Post_bootscamp, Post_community, Comment
from .forms import (
    CustomAuthenticationForm as AuthenticationForm, 
    CustomPasswordChangeForm as PasswordChangeForm,
    CustomUserChangeForm as UserChangeForm,
    CustomUserCreationForm as UserCreationForm,
    EditorForm
)
import math
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
        # else:
            # return redirect('accounts:login')            
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            # user = user.save()
            print(user)
            
            # current_site = get_current_site(request)
            current_site = request.META['HTTP_HOST'],
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site[0],
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = '계정 활성화 확인 이메일'
            mail_to = request.POST['email']
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            # auth_login(request, user)
            return render(request, 'accounts/success.html')
            return redirect('posts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('posts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST,request.FILES,instance=request.user)
        edit = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            editor = edit.save()
            return redirect('posts:index')
    else:
        form = UserChangeForm(instance=request.user)
        edit = EditorForm()
    context = {
        'form' : form,
        'edit' : edit,
    }
    return render(request,'accounts/update.html',context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
 
@login_required
def profile(request, user_pk):
    my_posts = Post_community.objects.filter(user=user_pk)
    my_posts_new = Post_community.objects.filter(user=request.user).order_by('-create_at')
    experience_max = int(math.log((request.user.level)*10) * 10)
    percent = int(((request.user.experience)/experience_max) * 100)
    percent_surplus = 100 - percent
    experience_surplus = (experience_max) - (request.user.experience)
    top_posts = Post_community.objects.annotate(like_count=Count('like_user')).filter(like_count__gte=3).order_by('-like_count')[:2]
    paginator = Paginator(my_posts_new, 5)  # 한 페이지에 표시할 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # my_comments = Comment.objects.filter(pk=user_pk)
    # print(my_posts)
    context = {
        'my_posts': my_posts,
        'my_posts_new': my_posts_new,
        'experience_max' : experience_max,
        'percent' : percent,
        'percent_surplus' : percent_surplus,
        'experience_surplus' : experience_surplus,
        'top_posts': top_posts,
        'page_obj' : page_obj,
        'page_number': page_number,  # 페이지 번호 변수 추가
        # 'my_comments': my_comments,
    }
    return render(request, 'accounts/profile.html', context)


# 테스트 용
def profile_note(request):
    return render(request, 'accounts/profile_note.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user is not None and account_activation_token.check_token(user, token):
            User.objects.filter(pk=uid).update(is_active=True)
            return redirect("posts:index")
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    else:
        return render(request, 'accounts/activation_email.html', {'error' : '계정 활성화 오류'})
    return 

def my_posts(request,user_pk):
    my_posts = Post_community.objects.filter(user=user_pk)
    my_posts_new = Post_community.objects.filter(user=request.user).order_by('-create_at')
    top_posts = Post_community.objects.annotate(like_count=Count('like_user')).filter(like_count__gte=3).order_by('-like_count')[:2]
    paginator = Paginator(my_posts_new, 5)  # 한 페이지에 표시할 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'my_posts': my_posts,
        'my_posts_new': my_posts_new,
        'top_posts': top_posts,
        'page_obj' : page_obj,
        'page_number': page_number,  # 페이지 번호 변수 추가
    }
    return render(request, 'accounts/my_posts.html',context)


def naver_login(request):
    return redirect('posts:index')