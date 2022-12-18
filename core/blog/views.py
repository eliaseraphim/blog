from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.filter(date_published__isnull=False).order_by('-date_published')
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)
