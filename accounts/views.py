from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


# Create your views here.

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('# post:index')
    template_name = 'accounts/create.html'
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = UserCreationForm
    success_url = reverse_lazy('account:detail')
    template_name = 'accounts/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('post:index')
    template_name = 'accounts/delete.html'