from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'account'
urlpatterns = [
    path('login/',LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # 로그인 뷰 // 로그인뷰만 템플릿 입력해야함
    path('logout/',LogoutView.as_view(),name='logout'),
    #
    path('create/',AccountCreateView.as_view(),name='create'),
    path('detail/<int:pk>',AccountDetailView.as_view(),name='detail'),
    path('update/<int:pk>',AccountUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',AccountDeleteView.as_view(),name='delete'),
]