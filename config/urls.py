""" The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/ """

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from page.views import home_view

urlpatterns = [
    path("", home_view, name="home_view"),

    # Blog:
    path("blog/", include('blog.urls', namespace='blog')),

    # Read:
    path("read/", include('read.urls', namespace='read')),

    # USER:
    path("user/", include('user_profile.urls', namespace='user')),

    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
