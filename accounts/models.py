from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class User(AbstractUser):
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

    def delete(self,*args,**kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT,self.image.path))
            dir_path = os.path.dirname(os.path.join(settings.MEDIA_ROOT, self.image.name))
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
        super(User, self).delete(*args,**kargs)

    def save(self,*args,**kwargs):
        if self.id:
            old_user = User.objects.get(id=self.id)
            if self.image != old_user.image:
                if old_user.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_user.image.path))
        super(User,self).save(*args,**kwargs)
        
        
class Editor(models.Model):
    text = RichTextUploadingField(blank=True, null=True)