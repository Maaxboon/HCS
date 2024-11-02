from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>" , views.greet, name="greet")
    path("Maaax", views.Maaax, name="Maaax"),
    path("Fanice", views.Fanice, name="Fanice")
]