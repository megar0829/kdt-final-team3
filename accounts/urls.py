from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/',views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name="change_password"),
    path('profile/<int:user_pk>/', views.profile, name="profile"),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('profile/<int:user_pk>/my_posts', views.my_posts, name="my_posts"),
    path('naver/login/?process=login/', views.naver_login, name='naver_login'),
    # 테스트 (프로필 쪽지)
    path('profile/note/', views.profile_note, name="profile_note")
]