from django import forms
from .models import Post_bootscamp, Post_community, Comment, Post_image, community_image

class PostForm(forms.Form):
    title = forms.CharField(label='부트캠프 제목', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='부트캠프 설명', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    start_data = forms.DateField(label='시작 날짜', widget=forms.DateInput(attrs={'type': 'date'}))
    duration = forms.IntegerField(label='기간 (일)', widget=forms.NumberInput(attrs={'class': 'form-control'}))

class PostImageForm(forms.ModelForm):
    class Meta:
        model = Post_image
        fields = ('post_image',)
        widgets = {forms.ClearableFileInput(attrs={'class': 'form-control-file'})}

POST_ADDRESS_CHOICES = (
     ("Django", "Django"), ("Java", "Java"), ("Spring", "Spring"),
    ("DB", "DB"), ("JPA", "JPA"), ("백엔드", "백엔드"), ("프론트엔드", "프론트엔드")
)

class CommunityForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력하세요'
            }
        )
    )

    content = forms.CharField(
        label="",
        widget= forms.Textarea(
            attrs={
                'placeholder': '내용을 입력하세요'
            }
        )
    )

    category = forms.ChoiceField(
        label="",
        choices=POST_ADDRESS_CHOICES,
        widget= forms.Select(
            attrs={
                'class': 'form-select',
            }
        )
    )
    class Meta:
        model = Post_community
        fields = ('category', 'title', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글 내용을 입력하세요',
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)

class CommuImageForm(forms.ModelForm):
    class Meta:
        model = community_image
        fields = ('community_image',)
        widgets = {forms.ClearableFileInput(attrs={'class': 'form-control-file'})}