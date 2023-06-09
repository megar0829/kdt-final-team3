from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post_bootscamp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)


    # 일정
    start_data1 =models.DateField()
    end_data = models.DateField()
    start_data2 = models.DateField()
    time = models.CharField(max_length=50)
    people = models.CharField(max_length=50)
    class_method = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    onoff = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    content = models.TextField()

    # 수강료
    price = models.CharField(max_length=50)
    card = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users')

    

class Post_community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    views = models.IntegerField(default=0)
    create_at =models.DateTimeField(auto_now_add=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_user')

    def comment_count(self):
        return self.comment.count()

    def increase_views(self):
        self.views += 1
        self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post_community, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


class Post_image(models.Model):
    post = models.ForeignKey(Post_bootscamp, on_delete=models.CASCADE, related_name='post_image')
    post_image = models.ImageField(upload_to='post_image/%Y/%m/%d/', blank=True, null=True)

class community_image(models.Model):
    community_post = models.ForeignKey(Post_community, on_delete=models.CASCADE)
    community_image = models.ImageField(upload_to='community_image/%Y/%m/%d/', blank=True, null=True)

class Editor(models.Model):
    text = RichTextUploadingField(blank=True, null=True)