from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    The default configuration for the blog application.

    .. py:attribute:: default_auto_field
        :type: str

        The implicit primary key type to add to models within this app. ::

            default_auto_field = 'django.db.models.BigAutoField'

    .. py:attribute:: name
        :type: str

        The name of the application. ::

            name = 'blog'
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
