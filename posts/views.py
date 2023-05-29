from django.shortcuts import render, redirect
from .models import Post_image, Post_bootscamp, Post_community, Comment, community_image
from .forms import PostForm, PostImageForm, CommunityForm, CommentForm, CommuImageForm

# Create your views here.

def index(request):
    boots = Post_bootscamp.objects.all()
    commu = Post_community.objects.all()
    context = {
        'boots':boots,
        'commu':commu,
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
        form = PostForm(request.POST)
        imageForm = PostImageForm(request.POST, request.FILES)
        if form.is_valid() and imageForm.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            start_data = form.cleaned_data['start_data']
            duration = form.cleaned_data['duration']
            bootcamp = Post_bootscamp(title=title, content=content, start_data=start_data, duration=duration)
            bootcamp.save()
            image = imageForm.cleaned_data['post_image']
            Post_image.objects.create(post=bootcamp, post_image=image)

            return redirect('posts:boots_detail', bootcamp.id)
    else:
        form = PostForm()
        imageForm = PostImageForm()
    context ={
        'form':form,
        'imageForm':imageForm
    }
    
    return render(request, 'posts/boots_create.html', context)

def bootscamp_detail(request, boots_pk):
    boots = Post_bootscamp.objects.get(pk=boots_pk)
    context = {
        'boots': boots,
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
    commu = Post_community.objects.all()
    top_posts = Post_community.objects.order_by('-views')[:3]
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
        'top_posts':top_posts,

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
            commu = Post_community(title=title, content=content, category=category)
            commu.save()
            image = imageform.cleaned_data['community_image']
            community_image.objects.create(community_post=commu, community_image=image)
        return redirect ('posts:commu_detail',commu.id)
    else:
        form = CommunityForm()
        imageform = community_image()
    
    context = {
        'form': form,
        'imageform': imageform,
    }
    return render(request, 'commun_info.html', context)

def community_detail(request, community_pk):
    commu = Post_community.objects.get(pk=community_pk)
    commu.increase_views()
    context = {
        'commu':commu
    }
    return render(request, 'posts/commu_detail.html', context)

def comment_create(request, community_pk):
    commu = Post_community.objects.get(pk=community_pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.user = request.user
        comment.commu = commu
        comment.save()
    return redirect('posts:commu_detail', community_pk)

def comment_delete(request, community_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('posts:commu_detail', community_pk)

def community_delete(request, community_pk):
    commu = Post_community.get(pk=community_pk)
    if request.user == commu.user:
        commu.delete()
    return redirect('posts:commu_info')

def community_update(request, community_pk):
    commu = Post_community.objects.get(pk=community_pk)
    if commu.user == request.user:
        if request.method == "POST":
            form = CommunityForm(request.POST, instance=commu)
            imageform = community_image(request.POST, request.FILES)
            if form.is_valid() and imageform.is_valid():
                form.save()
                commu.community_image.delete()
                image = imageform.cleaned_data['community_image']
                community_image.objects.create(post=commu, community_image=image)
                return redirect('posts:commu_detail',commu.id)
        else:
            form = CommunityForm(instance=commu)
            imageform = community_image()
        context = {
            'form': form,
            'imageform': imageform,
            'commu': commu,
        }
        return render(request, 'commu_update.html', context)
    else:
        return redirect('posts:commu_detail', commu_id=commu.id)

def community_like(request, community_pk):
    pass

def community_filter(request, category):
    commu = Post_community.objects.filter(category=category).order_by('-pk')
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
    }
    return render(request, "posts/commu_info.html", context)