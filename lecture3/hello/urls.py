from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("vlad", views.vlad, name="vlad"),
    path("ana", views.ana, name="ana")

]
