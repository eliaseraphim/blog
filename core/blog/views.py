from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    model = Post
    ordering = ['-id']

    context_object_name = 'posts'
    template_name = 'blog/index.html'


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        context = {
            'form': form
        }
    return render(request, 'blog/new_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        context = {
            'form': form
        }
    return render(request, 'blog/edit_post.html', context)