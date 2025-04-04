from django.contrib import admin
from django.urls import include, path

from college_app.api.views import accept_post, create_post, delete_post, my_posts_list, posts_list

urlpatterns = [
    path("posts/", posts_list),
    path("my_posts/", my_posts_list),
    path('create/', create_post),
    path("delete/<int:pk>", delete_post),
    path("accept/<int:pk>", accept_post)
]
