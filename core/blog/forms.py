from datetime import datetime

from django import forms
from django.utils import timezone

from .models import Post


# Widgets
class DateTimeWidget(forms.MultiWidget):
    """
    Widget for :py:attr:`blog.models.Post.date_published` form field in py:class:`PostForm`.

    .. py:attribute:: widgets
        :type: list

        Widgets for the ``django.forms.MultiWidget``. ::

            widgets = [
                forms.DateInput(attrs=date_input_attrs, format='%m/%d/%Y'),
                forms.TimeInput(attrs=attrs, format='%H:%M'),
            ]
    """
    def __init__(self, attrs=None):
        """
        Constructor for py:class:`DateTimeWidget`.

        :param attrs: Optional parameter. The HTML attributes for the form fields.
        :type attrs: ``dict`` or ``None``
        """
        date_input_attrs = {**attrs, 'type': 'date'} if attrs else {'type': 'date'}
        time_input_attrs = {**attrs, 'type': 'time'} if attrs else {'type': 'time'}
        widgets = [
            forms.DateInput(attrs=date_input_attrs, format='%m/%d/%Y'),
            forms.TimeInput(attrs=attrs, format='%H:%M'),
        ]

        super().__init__(widgets, attrs)

    def decompress(self, value):
        """
        Converts the ``datetime`` value from the :py:attr:`blog.models.Post.date_published` into a date and time object.

        :param value: :py:attr:`blog.models.Post.date_published`
        :type value: ``datetime.datetime`` if editing/deleting a post. ``None`` if creating a new post.
        :returns: A list containing the date and time objects.
        :rtype: ``list``
        """
        print(type(value))
        if isinstance(value, datetime):
            return [value.date(), value.time()]
        if isinstance(value, str):
            return value.split()
        return [None, None]

    def value_from_datadict(self, data, files, name):
        """
        Converts the ``date`` and ``time`` fields into a ``datetime`` string.

        TODO: Remove automatic setting for time once a better setup is created for selecting the time.

        :param data: The data from the form POST request.
        :type data: ``django.http.request.QueryDict``
        :param files: A dictionary of files. Should be empty.
        :type files: ``django.utils.datastructures.MultiValueDict``
        :param name: The name of the field.
        :type name: ``str``
        """
        date, time = super().value_from_datadict(data, files, name)
        if time:
            return f'{date} {time}'
        return f'{date} {timezone.now().strftime("%H:%M")}'


# Forms
class PostForm(forms.ModelForm):
    """Form for editing and deleting a Post. Extends :py:class:`django.forms.ModelForm`."""
    class Meta:
        """
        Metadata for :py:class:`PostForm`.

        .. py:attribute:: fields
            :type: tuple

            Form fields. ::

                fields = ('title', 'author', 'text', 'image', 'date_published')

        .. py:attribute:: widgets
            :type: dict

            Form widgets. ::

                model = Post
                fields = ('title', 'author', 'text', 'image', 'date_published')
                widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'author': forms.Select(attrs={'class': 'form-control'}),
                    'text': forms.Textarea(attrs={'class': 'form-control'}),
                    'date_published': DateTimeWidget(attrs={'class': 'form-control'}),
                }
        """
        model = Post
        fields = ('title', 'author', 'text', 'image', 'date_published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'date_published': DateTimeWidget(attrs={'class': 'form-control'}),
        }
