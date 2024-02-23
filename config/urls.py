""" The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/ """

from django.contrib import admin
from django.urls import path
from page.views import home_view

urlpatterns = [
    path("", home_view, name="home_view"),
    path("admin/", admin.site.urls),
]
