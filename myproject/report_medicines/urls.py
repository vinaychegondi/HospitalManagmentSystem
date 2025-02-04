# report_medicines/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_medicines, name='report_medicines'),  # Routes /report_medicines/ to the report_medicines view
]
