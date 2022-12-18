from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.filter(date_published__isnull=False).order_by('-date_published')
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)