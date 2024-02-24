from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", home, name='index'),
    path('create', new_post, name='new_post'),
    path('read/<int:post_id>', read_post, name='read_post'),
    path('edit/<int:post_id>', edit_post, name='edit_post'),
    path('del/<int:post_id>', delete_post, name='delete_post')
]
