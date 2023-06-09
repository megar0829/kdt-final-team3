from django.shortcuts import render, redirect
from .models import Post_image, Post_bootscamp, Post_community, Comment, community_image, Tag
from .forms import PostForm, PostImageForm, CommunityForm, CommentForm, CommuImageForm, EditorForm
from django.http import JsonResponse
from django.db import models
from django.db.models import Q


# Create your views here.

def index(request):
    boots = Post_bootscamp.objects.all()
    commu = Post_community.objects.all()
    # my_posts_new = Post_community.objects.filter(user=request.user).order_by('-create_at')
    context = {
        'boots':boots,
        'commu':commu,
        # 'my_posts_new':my_posts_new,
    }
    return render(request, 'posts/index.html', context)

def bootscamp_info(request):
    boots = Post_bootscamp.objects.all()
    context = {
        'boots':boots
    }
    return render(request, 'posts/boots_info.html', context)

def bootscamp_create(request):
    if request.method == 'POST':
        form = PostImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            tags = request.POST.getlist('tags')
            start_data1 = request.POST.get('start_data1')
            start_data2 = request.POST.get('start_data2')
            end_data = request.POST.get('end_data')
            time = request.POST.get('time')
            people = request.POST.get('people')
            class_method = request.POST.get('class_method')
            equipment = request.POST.get('equipment')
            onoff = request.POST.get('onoff')
            location = request.POST.get('location')
            content = request.POST.get('content')
            price = request.POST.get('price')
            card = request.POST.get('card')
            image = form.cleaned_data['post_image']

            bootcamp = Post_bootscamp.objects.create(
                user_id = request.user.pk,
                title=title,
                start_data1=start_data1,
                start_data2=start_data2,
                end_data=end_data,
                time=time,
                people=people,
                class_method=class_method,
                equipment=equipment,
                onoff=onoff,
                location=location,
                content=content,
                price=price,
                card=card,
            )

            Post_image.objects.create(post=bootcamp, post_image=image)

            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                bootcamp.tags.add(tag)

            return redirect('posts:boots_detail', bootcamp.id)
    else:
        form = PostImageForm()

    context = {
        'imageForm': form
    }
    return render(request, 'posts/boots_create.html', context)

def bootscamp_detail(request, boots_pk):
    post = Post_bootscamp.objects.get(pk=boots_pk)
    tags = Tag.objects.get(pk=boots_pk)
    context = {
        'post': post,
        'tags': tags,
    }
    return render(request, 'posts/boots_detail.html', context)

def bootscamp_update(request, boots_pk):
    boots = Post_bootscamp.objects.get(pk=boots_pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    boots.title = title
    boots.content = content
    boots.save()
    return redirect('posts:boots_detail')

def bootscamp_delete(request, boots_pk):
    boots = Post_bootscamp.objects.get(pk=boots_pk)
    if request.user == boots.user:
        boots.delete()
    return redirect('posts:boots_info')

def bootscamp_like(request, boots_pk):
    pass

def community_info(request):
    post_list = Post_community.objects.all().order_by('-pk')
    paginator = Paginator(post_list, 5)  # 한 페이지에 표시할 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # commu = Post_community.objects.all().order_by('-pk')
    top_posts = Post_community.objects.order_by('-views')[:2]

    commu_filtered = Post_community.objects.annotate(like_count=models.Count('like_user')).filter(like_count__gte=3)
    
    if request.method == 'POST':
        commu_create = CommunityForm(request.POST)
        commu_image = CommuImageForm(request.POST, request.FILES)
    else:
        commu_create = CommunityForm()
        commu_image = CommuImageForm()
    context = {
        'commu': page_obj,
        'commu_create':commu_create,
        'commu_image':commu_image,
        'top_posts':top_posts,
        'commu_filtered': commu_filtered,  # 추천글 (좋아요3개이상)

    }
    return render(request, 'posts/commu_info.html', context)

def community_create(request):
    if request.method == "POST":
        form = CommunityForm(request.POST)
        imageform = CommuImageForm(request.POST, request.FILES)
        if form.is_valid() and imageform.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            commu = Post_community(title=title, content=content, category=category, user_id=request.user.pk)
            commu.save()
            image = imageform.cleaned_data['community_image']
            community_image.objects.create(community_post=commu, community_image=image)
        return redirect ('posts:commu_detail', commu.id)
    else:
        form = CommunityForm()
        imageform = CommuImageForm()
    
    context = {
        'form': form,
        'imageform': imageform,
    }
    return render(request, 'commun_info.html', context)

def community_detail(request, community_pk):
    commus = Post_community.objects.get(pk=community_pk)
    commus.increase_views()
    commu_list = Post_community.objects.exclude(pk=community_pk).order_by('-pk')
    commu_filtered = Post_community.objects.annotate(like_count=models.Count('like_user')).filter(like_count__gte=3)
    context = {
        'commus': commus,
        'commu_list': commu_list,
        'commu_filtered': commu_filtered,  # 추천글 (좋아요3개이상)
    }
    return render(request, 'posts/commu_detail.html', context)


def comment_create(request, community_pk):
    commu = Post_community.objects.get(pk=community_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = commu  # post 필드에 commu 값을 할당
            comment.user = request.user
            comment.content = content
            comment.save()
    return redirect('posts:commu_detail', community_pk)

def comment_delete(request, community_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('posts:commu_detail', community_pk)

def community_delete(request, community_pk):
    commu = Post_community.objects.get(pk=community_pk)
    if request.user == commu.user:
        commu.delete()
    return redirect('posts:commu_info')

def community_update(request, community_pk):
    commu = Post_community.objects.get(pk=community_pk)
    if commu.user == request.user:
        if request.method == "POST":
            form = EditorForm(request.POST, instance=commu)
            imageform = CommuImageForm(request.POST, request.FILES)
            if form.is_valid() and imageform.is_valid():
                form.save()
                image = imageform.cleaned_data['community_image']
                community_image.objects.create(community_post=commu, community_image=image)
                return redirect('posts:commu_detail', commu.id)
        else:
            form = EditorForm(instance=commu)
            imageform = CommuImageForm()
        context = {
            'form': form,
            'imageform': imageform,
            'commu': commu,
        }
        return render(request, 'posts/commu_update.html', context)
    else:
        return redirect('posts:commu_detail', commu.id)

def community_like(request, community_pk):
    post = Post_community.objects.get(pk=community_pk)
    if request.user in post.like_user.all():
        post.like_user.remove(request.user)
        is_like_user = False
    else:
        post.like_user.add(request.user)
        is_like_user = True
    post.like_count = post.like_user.count()  # 좋아요 개수 업데이트
    print(post.pk)
    post.save()
    context = {
        'is_like_user':is_like_user,
        'like_count': post.like_user.count()  # 좋아요 개수를 추가
    }
    return JsonResponse(context)

def community_filter(request, category):
    commu = Post_community.objects.filter(category=category).order_by('-pk')
    commu_filtered = Post_community.objects.annotate(like_count=models.Count('like_user')).filter(like_count__gte=3)
    if request.method == 'POST':
        commu_create = CommunityForm(request.POST)
        commu_image = CommuImageForm(request.POST, request.FILES)
    else:
        commu_create = CommunityForm()
        commu_image = CommuImageForm()
    context = {
        'commu':commu,
        'commu_create':commu_create,
        'commu_image':commu_image,
        'commu_filtered': commu_filtered,  # 추천글 (좋아요3개이상)
    }
    return render(request, "posts/commu_info.html", context)

def community_info_best(request):
    commu = Post_community.objects.all().order_by('-pk')
    top_posts_all = Post_community.objects.order_by('-views')[:5]
    commu_filtered = Post_community.objects.annotate(like_count=models.Count('like_user')).filter(like_count__gte=3)
    if request.method == 'POST':
        commu_create = CommunityForm(request.POST)
        commu_image = CommuImageForm(request.POST, request.FILES)
    else:
        commu_create = CommunityForm()
        commu_image = CommuImageForm()
    context = {
        'commu':commu,
        'commu_create':commu_create,
        'commu_image':commu_image,
        'top_posts_all':top_posts_all,
        'commu_filtered': commu_filtered,  # 추천글 (좋아요3개이상)
    }
    return render(request, 'posts/commu_info_best.html', context)

def community_info_new(request):
    post_list = Post_community.objects.all().order_by('-pk')
    paginator = Paginator(post_list, 5)  # 한 페이지에 표시할 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # commu = Post_community.objects.all().order_by('-pk')
    top_posts = Post_community.objects.order_by('-views')[:4]
    commu_filtered = Post_community.objects.annotate(like_count=models.Count('like_user')).filter(like_count__gte=3)
    if request.method == 'POST':
        commu_create = CommunityForm(request.POST)
        commu_image = CommuImageForm(request.POST, request.FILES)
    else:
        commu_create = CommunityForm()
        commu_image = CommuImageForm()
    context = {
        'commu': page_obj,
        'commu_create':commu_create,
        'commu_image':commu_image,
        'top_posts':top_posts,
        'commu_filtered': commu_filtered,  # 추천글 (좋아요3개이상)

    }
    return render(request, 'posts/commu_info_new.html', context)

from django.core.paginator import Paginator

def community_list(request):
    post_list = Post_community.objects.all()
    paginator = Paginator(post_list, 5)  # 한 페이지에 표시할 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'commu': page_obj,  # commu 변수를 page_obj로 변경
    }
    return render(request, 'posts/community_list.html', context)

def search(request, keyword):
    keyword = request.GET.get('keyword')
    commu = Post_community.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword)).order_by('-pk')
    context = {
        'commu':commu,
        'keyword':keyword,
    }
    return render(request, 'posts/commu_info.html', context)

def community_info_like(request):
    post_list = Post_community.objects.all().order_by('-pk')
    paginator = Paginator(post_list, 5)  # 한 페이지에 표시할 게시글 수를 5로 설정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # commu = Post_community.objects.all().order_by('-pk')
    top_posts = Post_community.objects.order_by('-views')[:4]
    commu_filtered = Post_community.objects.annotate(like_count=models.Count('like_user')).filter(like_count__gte=3)

    if request.method == 'POST':
        commu_create = CommunityForm(request.POST)
        commu_image = CommuImageForm(request.POST, request.FILES)
    else:
        commu_create = CommunityForm()
        commu_image = CommuImageForm()
    context = {
        'commu': page_obj,
        'commu_create':commu_create,
        'commu_image':commu_image,
        'top_posts':top_posts,
        'commu_filtered': commu_filtered,  # 추천글 (좋아요3개이상)

    }
    return render(request, 'posts/commu_info_like.html', context)