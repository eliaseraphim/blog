from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.detail, name='detail'),
    path('post/new', views.new_post, name='new_post'),
    path('post/<int:pk>/edit', views.edit_post, name='edit_post')
]
