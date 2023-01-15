from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    """
    The view class for the index view of the blog.

    .. py:attribute:: context_object_name
        :type: str

        The name of the object attached to the context data. ::

            context_object_name = 'posts'

    .. py:attribute:: template_name
        :type: str

        The name of the template used for the view. ::

            template_name = 'blog/index.html'
    """
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        """
        Return a :py:class:`QuerySet` of posts.

        :returns: A set of Posts published before the ``timezone.now()`` ordered by :py:attr:`blog.models.Post.date_published` (descending).
        :rtype: :py:class:`QuerySet`
        """
        return Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')


class DetailView(generic.DetailView):
    """
    The view class for the detail view of a post.

    .. py:attribute:: context_object_name
        :type: str

        The name of the object attached to the context data. ::

            context_object_name = 'posts'

    .. py:attribute:: template_name
        :type: str

        The name of the template used for the view. ::

            template_name = 'blog/detail.html'
    """
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'


class NewPostView(LoginRequiredMixin, generic.CreateView):
    """
    The view class for the create view of a post.

    .. py:attribute:: context_object_name
        :type: str

        The name of the object attached to the context data. ::

            context_object_name = 'form'

    .. py:attribute:: template_name
        :type: str

        The name of the template used for the view. ::

            template_name = 'blog/post/actions/edit.html'
    """
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    template_name = 'blog/post/actions/edit.html'

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context data, with additional context for the action button.

        :returns: ``context_data``
        :rtype: :py:class:`dict`
        """
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'form_action': 'Save Post',
            'button_text': 'Save',
        })

        return context_data

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form. Returns to py:class:`IndexView`."""
        return reverse('index')


class EditPostView(LoginRequiredMixin, generic.UpdateView):
    """
    The view class for the update view of a post.

    .. py:attribute:: context_object_name
        :type: str

        The name of the object attached to the context data. ::

            context_object_name = 'form'

    .. py:attribute:: template_name
        :type: str

        The name of the template used for the view. ::

            template_name = 'blog/post/actions/edit.html'
    """
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    template_name = 'blog/post/actions/edit.html'

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context data, with additional context for the action button.

        :returns: ``context_data``
        :rtype: :py:class:`dict`
        """
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'form_action': 'Edit Post',
            'button_text': 'Edit',
        })

        return context_data

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form. Returns to py:class:`IndexView`."""
        return reverse('index')


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    """
    The view class for the delete view of a post.

    .. py:attribute:: context_object_name
        :type: str

        The name of the object attached to the context data. ::

            context_object_name = 'form'

    .. py:attribute:: template_name
        :type: str

        The name of the template used for the view. ::

            template_name = 'blog/post/actions/delete.html'
    """
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post/actions/delete.html'

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context data, with additional context for the action button.

        :returns: ``context_data``
        :rtype: :py:class:`dict`
        """
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'form_action': 'Delete Post',
            'button_text': 'Delete',
        })

        return context_data

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form. Returns to :py:class:`IndexView`."""
        return reverse('index')
