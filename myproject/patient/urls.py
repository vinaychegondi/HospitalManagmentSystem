# patient/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_view, name='patient'),  # This routes /patient/ to patient_view
]
