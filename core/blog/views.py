from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    """
    .. py:class:: IndexView
        The view class for the index page of the blog. Inherits from :py:class:`django.views.generic.ListView`.

        :cvar :py:class:`django.db.Model` model: The model for the view. Set to: :py:class:`blog.models.Post`
        :cvar :py:class:`str` context_object_name: The name of the object returned by :py:meth:`get_context_data(self, **kwargs)`. Set to: ``'posts'``.
        :cvar :py:class:`str` template_name: The name of the template for the view. Set to: ``'blog/index.html'``.
    """

    model = Post

    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        """
        Return a :py:class:`QuerySet` of posts.

        :returns: A set of Posts ordered by :py:attr:`date_published` (descending).
        :rtype: :py:class:`QuerySet`
        """
        return Post.objects.filter(date_published__isnull=False).order_by('-date_published')


class DetailView(generic.DetailView):
    model = Post

    context_object_name = 'post'
    template_name = 'blog/detail.html'


class NewPostView(generic.CreateView):
    model = Post
    form_class = PostForm

    context_object_name = 'form'
    template_name = 'blog/post/actions/edit.html'

    def get_success_url(self):
        return reverse('index')


class EditPostView(generic.UpdateView):
    model = Post
    form_class = PostForm

    context_object_name = 'form'
    template_name = 'blog/post/actions/edit.html'

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context dict, with additional context for action button.

        :returns: ``context_data``
        :rtype: ``dict``
        """

        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'form_action': 'Edit Post',
            'button_text': 'Edit',
        })

        return context_data

    def get_success_url(self):
        return reverse('index')


class DeletePostView(generic.DeleteView):
    """

    """
    model = Post

    context_object_name = 'post'
    template_name = 'blog/post/actions/delete.html'

    def get_context_data(self, **kwargs):
        """
        This function gets the context data for the view.

        We attach 'form_action' and 'button_text' for the action bar.
        """
        print(kwargs)
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'form_action': 'Delete Post',
            'button_text': 'Delete',
        })

        return context_data

    def get_success_url(self):
        return reverse('index')