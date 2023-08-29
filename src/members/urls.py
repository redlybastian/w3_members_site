from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path("members/main", views.main, name="main"),
    path("template/", views.testing, name="template"),
    path("template/<int:id>", views.testing, name="template"),
    path("members/", views.members, name="members"),
    path("members/details/<int:id>", views.details, name="details"),
]
