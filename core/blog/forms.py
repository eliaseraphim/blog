from django import forms
from django.utils import timezone

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'text', 'image', 'date_published')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'date_published': forms.DateInput(attrs={'class:': 'form-control', 'placeholder': f'{timezone.now()}'})
        }
