from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import ProjectPost

# Create your views here.
def index(request):
    all_posts = ProjectPost.objects.all()
    
    context = {
        'all_posts' : all_posts
    }

    return render(request, 'main/index.html', context) 

def about(request):

    return render(request, 'main/about.html', {}) 

def linkedin(request):

    return redirect('https://www.linkedin.com/in/daniel-ragsdale-503080116')
