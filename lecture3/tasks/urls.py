from django.urls import path
from . import views

app_name = "tasks" #Esto se agrega para evita name collisions con index de otras apps
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]