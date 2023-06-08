from django.shortcuts import render, redirect
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
from django.db.models import Count

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
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
            auth_login(request, user)
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
            return redirect('posts:index', editor.pk)
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
    # my_profile = User.objects.get(pk=user_pk)
    my_posts = Post_community.objects.filter(user=user_pk)
    top_posts = Post_community.objects.annotate(like_count=Count('like_user')).filter(like_count__gte=3).order_by('-like_count')[:2]
    # my_comments = Comment.objects.filter(pk=user_pk)
    # print(my_posts)
    context = {
        'my_posts': my_posts,
        'top_posts': top_posts,
        # 'my_comments': my_comments,
    }
    return render(request, 'accounts/profile.html', context)


# 테스트 용
def profile_note(request):
    return render(request, 'accounts/profile_note.html')

