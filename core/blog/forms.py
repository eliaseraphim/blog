from django import forms

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

                fields = ('title', 'text', 'image')

        .. py:attribute:: widgets
            :type: dict

            Form widgets. ::

                model = Post
                fields = ('title', 'text', 'image')
                widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'text': forms.Textarea(attrs={'class': 'form-control'}),
                    'date_published': DateTimeWidget(attrs={'class': 'form-control'}),
                }
        """

        model = Post
        fields = ["title", "text", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
