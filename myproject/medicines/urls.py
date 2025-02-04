# medicines/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('prescription/', views.prescription_view, name='prescription'),  # URL for adding medicines to a prescription
]
