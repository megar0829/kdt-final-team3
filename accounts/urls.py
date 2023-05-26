from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'account'
urlpatterns = [
    path('login/',, name='login'),
    path('logout/',,name='logout'),
    #
    path('create/',,name='create'),
    path('detail/<int:pk>',,name='detail'),
    path('update/<int:pk>',,name='update'),
    path('delete/<int:pk>',,name='delete'),
]