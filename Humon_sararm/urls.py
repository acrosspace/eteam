from django.urls import path
from Humon_sararm import views
urlpatterns = [
    path("", views.index, name="index"),
]
