from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    """The view class for the index page of the blog. Inherits from :py:class:`django.views.generic.ListView`."""

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
    """The view class for the detail page of a post. Inherits from :py:class:`django.views.generic.DetailView`."""

    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'


class NewPostView(generic.CreateView):
    """The view class for creating a new post. Inherits from :py:class:`django.views.generic.CreateView`."""

    model = Post
    form_class = PostForm
    context_object_name = 'form'
    template_name = 'blog/post/actions/edit.html'

    def get_success_url(self):
        return reverse('index')


class EditPostView(generic.UpdateView):
    """The view class for editing a post. Inherits from :py:class:`django.views.generic.UpdateView`."""

    model = Post
    form_class = PostForm
    context_object_name = 'form'
    template_name = 'blog/post/actions/edit.html'

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context data, with additional context for the action button.

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
        """Return the URL to redirect to after processing a valid form. Returns to :py:class:`blog.views.IndexView`."""

        return reverse('index')


class DeletePostView(generic.DeleteView):
    """The view class for deleting a post. Inherits from :py:class:`django.views.generic.DeleteView`."""

    model = Post
    context_object_name = 'post'
    template_name = 'blog/post/actions/delete.html'

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context data, with additional context for the action button.

        :returns: ``context_data``
        :rtype: ``dict``
        """

        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'form_action': 'Delete Post',
            'button_text': 'Delete',
        })

        return context_data

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form. Returns to :py:class:`blog.views.IndexView`."""

        return reverse('index')
