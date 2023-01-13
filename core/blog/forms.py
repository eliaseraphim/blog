from django import forms

from .models import Post


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

                widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'author': forms.Select(attrs={'class': 'form-control'}),
                    'text': forms.Textarea(attrs={'class': 'form-control'}),
                    'date_published': forms.DateTimeInput(
                        format='%m/%d/%Y %H:%M',
                        attrs={'class': 'form-control', 'type': 'datetime'}
                    ),
                }
        """
        model = Post
        fields = ('title', 'author', 'text', 'image', 'date_published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'date_published': forms.DateTimeInput(
                format='%m/%d/%Y %H:%M',
                attrs={'class': 'form-control', 'type': 'datetime'}
            ),
        }
