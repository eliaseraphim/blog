from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField (blank=True, null=True)

    def __str__(self):
        return self.title
