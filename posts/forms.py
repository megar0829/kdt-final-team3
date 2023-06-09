from django import forms
from .models import Post_bootscamp, Post_community, Comment, Post_image, community_image, Editor
from ckeditor.widgets import CKEditorWidget


CARD_ADDRESS_CHOICES = (
    ("필요", "내일배움카드가 필요해요"), ("불필요", "내일배움카드 필요없어요")
)

class PostForm(forms.ModelForm):
    title = forms.CharField(label='부트캠프 제목', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_data1 = forms.DateField(label='마감 날짜', widget=forms.DateInput(attrs={'type': 'date'}))
    start_data2 = forms.DateField(label='시작 날짜', widget=forms.DateInput(attrs={'type': 'date'}))
    end_data = forms.DateField(label='종강 날짜', widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.CharField(label='수업 시간', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    people = forms.CharField(label='모집 인원', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class_method = forms.CharField(label='수업 장소', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    equipment = forms.CharField(label='수업 장비', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    onoff = forms.CharField(label='온 / 오프', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='장소', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='부트캠프 설명', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    price = forms.CharField(label='수강료', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    card = forms.CharField(label='내카배', widget=forms.Select(choices=CARD_ADDRESS_CHOICES, attrs={'class': 'form-select'}))
    class Meta:
        model = Post_bootscamp
        fields = ('title', 'start_data1', 'start_data2', 'end_data', 'time', 'people', 'class_method', 'equipment', 'onoff', 'location', 'content', 'price', 'card')


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

