from django.urls import path
from . import views

urlpatterns = [
    path('', views.carryid, name='carryid'),  # Maps to /carryid/
]
