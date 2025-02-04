# Room_allotment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_allotment, name='room_allotment'),  # Routes /room_allotment/ to the room_allotment view
]
