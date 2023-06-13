from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(
        max_length=10,
        # null=True,
        # unique=False,
        error_messages={
            'unique': ("이미 사용 중인 닉네임입니다."),
        },
    )
    
    # 경험치 바 
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)

    def profile_image_path(instance,filename):
        return f'accounts/{instance.pk}/{filename}'

    image = ProcessedImageField(
        upload_to = 'profile/%Y%m',
        processors = [
            ResizeToFill(100,100),
            ],
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True,
    )

    def delete(self,*args,**kwargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT,self.image.path))
            dir_path = os.path.dirname(os.path.join(settings.MEDIA_ROOT, self.image.name))
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
        super(User, self).delete(*args,**kwargs)

    def save(self,*args,**kwargs):
        if self.id:
            old_user = User.objects.get(id=self.id)
            if self.image != old_user.image:
                if old_user.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_user.image.path))
        super(User,self).save(*args,**kwargs)
        
        
class Editor(models.Model):
    text = RichTextUploadingField(blank=True, null=True)