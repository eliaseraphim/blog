from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.detail, name='detail'),
    path('post/new', views.new_post, name='new_post')
]
