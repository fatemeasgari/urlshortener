from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("shorten", views.shorten, name='shorten'),
    path("created", views.created, name='created'),
]
