from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name= "title"),
    path("search", views.search, name= "search"),
    path("newpage", views.new_enry, name="createnewpage"),
    path("random", views.random_page, name="randompage"),
    path("wiki/<str:titlee>/edit", views.edit_page, name="editpage")
]
