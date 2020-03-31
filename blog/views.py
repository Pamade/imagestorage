from django.shortcuts import render
from .models import Post
from users.models import Media

def home(request):
    if request.method == 'GET':
        media_images = Media.objects.all()
    context = {
        'posts': Post.objects.all(),
        'media_images':media_images
    }


    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
