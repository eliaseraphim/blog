from django.contrib import admin

from .models import Post


class BlogAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Post)
