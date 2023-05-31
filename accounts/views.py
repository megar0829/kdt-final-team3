from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, "accounts/signup.html")

def login(request):
    return render(request, "accounts/login.html")

def profile(request):
    return render(request, "accounts/profile.html")

def profile_note(request):
    return render(request, "accounts/profile_note.html")