from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.post_create, name='create'),
    path('post/', views.bootscampinfo, name='bootsinfo'),
    path('<int:post_pk>/', views.post_detail, name='post_detail'),
    path('<int:post_pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:post_pk>/update/', views.post_update, name='post_update'),
    path('<int:post_pk>/like/', views.like_post, name='like_post'),
    path('community/', views.communityinfo, name='commuinfo'),
    path('community/<int:community_pk>/', views.community_detail, name='commu_detail'),
    path('community/<int:community_pk>/comment/', views.comment_create, name='comment'),
    path('community/<int:community_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('community/<int:community_pk>/delete/', views.community_delete, name='commu_delete'),
    path('community/<int:community_pk>/update/', views.community_update, name='commu_update'),
    path('community/<int:community_pk>/like/', views.like_community, name='like_commu'),
]
