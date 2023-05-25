from django import forms
from .models import Post_bootscamp, Post_community, Comment, Post_image

class postForm(forms.modelForm):
    class Meta:
        model = Post_bootscamp
        fields = (
            'title',
            'content',
            
        )
    
