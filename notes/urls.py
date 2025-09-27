from django.contrib import admin
from . import views
from django.urls import include, path


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("delete/<int:id>/", views.delete, name="delete"), #int:id will pass the integer id as pk so that only that one would be deleted e.g "delete/3/"
    path("edit/<int:id>/", views.edit, name="edit"),
]