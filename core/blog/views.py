from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    model = Post
    ordering = ['-id']

    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(date_published__isnull=False).order_by('-date_published')


class DetailView(generic.DetailView):
    model = Post

    context_object_name = 'post'
    template_name = 'blog/detail.html'


class NewPostView(generic.CreateView):
    model = Post
    form_class = PostForm

    context_object_name = 'form'
    template_name = 'blog/edit_post.html'

    def get_success_url(self):
        return reverse('index')


class EditPostView(generic.UpdateView):
    model = Post
    form_class = PostForm

    context_object_name = 'form'
    template_name = 'blog/edit_post.html'

    def get_success_url(self):
        return reverse('index')


class DeletePostView(generic.DeleteView):
    model = Post

    template_name = 'blog/delete_post.html'

    def get_success_url(self):
        return reverse('index')