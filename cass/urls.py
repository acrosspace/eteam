from django.urls import path
from cass import views
urlpatterns = [
    path("", views.index, name="index"),
]