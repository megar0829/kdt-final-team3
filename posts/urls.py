from django.urls import path, re_path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('boots/', views.bootscamp_info, name='boots_info'),
    path('boots/create/', views.bootscamp_create, name='boots_create'),
    path('boots/<int:boots_pk>/', views.bootscamp_detail, name='boots_detail'),
    path('boots/<int:boots_pk>/delete/', views.bootscamp_delete, name='boots_delete'),
    path('boots/<int:boots_pk>/update/', views.bootscamp_update, name='boots_update'),
    path('boots/<int:boots_pk>/like/', views.bootscamp_like, name='boots_like'),
    path('community/', views.community_info, name='commu_info'),
    path('community/create/', views.community_create, name='commu_create'),
    path('community/<int:community_pk>/', views.community_detail, name='commu_detail'),
    path('community/<int:community_pk>/delete/', views.community_delete, name='commu_delete'),
    path('community/<int:community_pk>/update/', views.community_update, name='commu_update'),
    path('community/<int:community_pk>/like/', views.community_like, name='commu_like'),
    path('community/<int:community_pk>/comment/', views.comment_create, name='comment'),
    path('community/<int:community_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('community/filter/<str:category>/', views.community_filter, name='commu_filter'),
    path('community/best/',views.community_info_best, name="commu_info_best"),
    path('community/new/',views.community_info_new, name="commu_info_new"),
    path('community/search/<str:keyword>', views.search, name='search'),

]
