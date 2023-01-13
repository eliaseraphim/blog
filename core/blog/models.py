from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Model for a blog post.

    .. py:attribute:: author

        The author of the post, defaults to: ::

            django.db.models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    .. py:attribute:: title

        The title of the post, defaults to: ::

            django.db.models.CharField(max_length=200)

    .. py:attribute:: text

        The plaintext of the post, defaults to: ::

            django.db.models.TextField()

    .. py:attribute:: image

        The image associated with the post defaults to: ::

            django.db.models.ImageField(blank=true, null=True, upload_to='images/%Y/%m/%d')

    .. py:attribute:: date_created

        The date and time the post was created, defaults to: ::

            django.db.models.DateTimeField(default=timezone.now)

    .. py:attribute:: date_published

        The date and time the post was published, defaults to: ::

            django.db.models.DateTimeField(blank=True, null=True)
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField (blank=True, null=True)

    def __str__(self):
        """
        Returns the ``str`` version of the Post object.

        :returns: :py:attr:`title`
        :rtype: :py:class:`str`
        """
        return self.title
