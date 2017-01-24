from django.shortcuts import render
from django.http import HttpResponse
from projects.models import ProjectPost

# Create your views here.
def index(request):
    all_posts = ProjectPost.objects.all()
    context = {
        'all_posts' : all_posts
    }

    return render(request, 'main/index.html', context) 
