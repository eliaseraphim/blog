from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('post/new', views.NewPostView.as_view(), name='new_post'),
    path('post/edit/<int:pk>', views.EditPostView.as_view(), name='edit_post')
]
