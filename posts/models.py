from django.db import models
from django.conf import settings
import math
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post_bootscamp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_data = models.DateField()
    duration = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
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

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.experience += 1
            self.user.save()
        if self.user.experience >= math.log((self.user.level)*10) * 10:
            self.user.level += 1
            self.user.save()
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post_community, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.experience += 1
            self.user.save()
        if self.user.experience >= math.log((self.user.level)*10) * 10:
            self.user.level += 1
            self.user.save()
        super().save(*args, **kwargs)

    # 경험치 바를 위한 save 재정의

class Post_image(models.Model):
    post = models.ForeignKey(Post_bootscamp, on_delete=models.CASCADE, related_name='post_image')
    post_image = models.ImageField(upload_to='post_image/%Y/%m/%d/', blank=True, null=True)

class community_image(models.Model):
    community_post = models.ForeignKey(Post_community, on_delete=models.CASCADE)
    community_image = models.ImageField(upload_to='community_image/%Y/%m/%d/', blank=True, null=True)

class Editor(models.Model):
    text = RichTextUploadingField(blank=True, null=True)