from django.urls import path
from rl_rxoh import views
urlpatterns=[
    path("",views.index, name="index"),
]