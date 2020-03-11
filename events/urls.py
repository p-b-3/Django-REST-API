from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ConferenceList.as_view()),
    path("<int:pk>", views.ConferenceDetail.as_view()),
    path("people", views.PeopleList.as_view())
]
