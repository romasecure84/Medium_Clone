from django.urls import path
from .views import create_blog_post_view, category_view, tag_view, fav_update_view, post_edit_view

app_name = 'blog'

urlpatterns = [
    path("create/", create_blog_post_view, name="create_blog_post_view"),
    path("category/<slug:category_slug>/", category_view, name="category_view"),
    path("tag/<slug:tag_slug>/", tag_view, name="tag_view"),

    path('post/<slug:post_slug>/edit/', post_edit_view, name='post_edit_view'),

    path("fav-update/", fav_update_view, name="fav_update_view"),
]
