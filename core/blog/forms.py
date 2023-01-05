from django import forms
from django.utils import timezone

from .models import Post

def get_current_time():
    current_time = str(timezone.now().date())
    print(current_time)

class PostForm(forms.ModelForm):
    class Meta:
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


