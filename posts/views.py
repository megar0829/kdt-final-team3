from django.shortcuts import render, redirect
from .models import Post_image, Post_bootscamp, Post_community, Comment

# Create your views here.

def index(request):
    posts = Post_bootscamp.objects.all()
    commu = Post_community.objects.all()
    context = {
        'posts':posts,
        'commu':commu,
    }
    return render(request, 'posts/index.html', context)

def bootscampinfo(request):
    posts = Post_bootscamp.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/bootscampinfo.html', context)

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post_bootscamp(title=title, content=content)
    post.save()
    return redirect('posts:bootscampinfo')

def post_detail(request, post_pk):
    post = Post_bootscamp.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)

def post_update(request, post_pk):
    post = Post_bootscamp.objects.get(pk=post_pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    post.title = title
    post.content = content
    post.save()
    return redirect('posts:post_detail')

def post_delete(request, post_pk):
    post = Post_bootscamp.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:bootscampinfo')

def like_post(request, post_pk):
    pass

def communityinfo(requset):
    commu = Post_community.objects.all()
    context = {
        'commu':commu
    }
    return render(requset, 'posts/communityinfo.html', context)

def community_detail(request, community_pk):
    commu = Post_community.get(pk=community_pk)
    context = {
        'commu':commu
    }
    return render(request, 'posts/community_detail.html', context)

def comment_create(request, community_pk):
    pass

def comment_delete(request, community_pk, comment_pk):
    pass

def community_delete(request, community_pk):
    commu = Post_community.get(pk=community_pk)
    if request.user == commu.user:
        commu.delete()
    return redirect('posts:commnuityinfo')

def community_update(request, community_pk):
    pass

def like_community(request, community_pk):
    pass