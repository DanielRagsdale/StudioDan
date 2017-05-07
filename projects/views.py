from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectPost

# Create your views here.
def index(request):
    all_posts = ProjectPost.objects.all()
    context = {
        'all_posts' : all_posts
    }

    return render(request, 'projects/index.html', context) 

def detail(request, project_slug):
    post = ProjectPost.objects.get(slug=project_slug.lower())
    
    context = {
        'post' : post
    }

    return render(request, 'projects/detail.html', context)
