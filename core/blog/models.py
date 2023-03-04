from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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

    .. py:attribute:: created

        The date and time the post was created, defaults to: ::

            created = models.DateTimeField(default=timezone.now, verbose_name=_("Date & Time Created"))

    .. py:attribute:: last_edited

        The date and time the post was last edited, defaults to: ::

            last_edited = models.DateTimeField(default=timezone.now, verbose=_("Date & Time Created"))
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        help_text=_("Author of the post."),
        null=True,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(help_text=_("Title of the post."), max_length=200)
    text = models.TextField(help_text=_("Text of the post."))
    image = models.ImageField(
        blank=True,
        help_text=_("Image uploaded with post."),
        null=True,
        upload_to="images/%Y/%m/%d",
    )
    created = models.DateTimeField(
        default=timezone.now, verbose_name=_("Date & Time Created")
    )
    last_edited = models.DateTimeField(
        auto_now=True, verbose_name=_("Date & Time Last Edited")
    )

    def __str__(self):
        """
        Returns the ``str`` version of the Post object.

        :returns: :py:attr:`title`
        :rtype: :py:class:`str`
        """
        return self.title

    @classmethod
    def get_authors_posts(cls, author):
        return cls.objects.filter(author_id=author.id).order_by("-created")
