# Pat_Prescription_Details/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pat_prescription_view, name='pat_prescription_view'),  # Routes /pat_prescription/ to the pat_prescription_view
]
