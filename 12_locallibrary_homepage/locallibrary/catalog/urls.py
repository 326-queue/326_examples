from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]

urlpatterns += [
   path("events", views.events, name="events")
]