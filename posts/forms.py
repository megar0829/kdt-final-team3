from django import forms
from .models import Post_bootscamp, Post_community, Comment, Post_image, community_image, Editor
from ckeditor.widgets import CKEditorWidget

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
    ("DB", "DB"), ("JPA", "JPA"), ("백앤드", "백앤드"), ("프론트앤드", "프론트앤드")
)

class CommunityForm(forms.ModelForm):
    category = forms.CharField(
        label="커뮤니티를 선택하세요",
        widget= forms.Select(
            choices= POST_ADDRESS_CHOICES,
            attrs={
                'class': 'form-select',
            }
        )
    )
    class Meta:
        model = Post_community
        fields = (
            'category',
            'title',
            'content',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class CommuImageForm(forms.ModelForm):
    class Meta:
        model = community_image
        fields = ('community_image',)
        widgets = {forms.ClearableFileInput(attrs={'class': 'form-control-file'})}

class EditorForm(forms.ModelForm):
    content = forms.CharField(
        label= "",
        widget=CKEditorWidget()
    )

    title = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={
                'style': 'width:100%;'
            }
        )
    )
    class Meta:
        model = Post_community
        fields = ('title','content' )

