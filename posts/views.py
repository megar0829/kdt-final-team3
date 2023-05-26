from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def commu(request):
    return render(request, "posts/commu.html")