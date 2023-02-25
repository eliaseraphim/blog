from datetime import datetime

from django import forms
from django.utils import timezone

from .models import Post


# Forms
class PostForm(forms.ModelForm):
    """Form for editing and deleting a Post. Extends :py:class:`django.forms.ModelForm`."""

    class Meta:
        """
        Metadata for :py:class:`PostForm`.

        .. py:attribute:: fields
            :type: tuple

            Form fields. ::

                fields = ('title', 'author', 'text', 'image')

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
        fields = ("title", "text", "image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
