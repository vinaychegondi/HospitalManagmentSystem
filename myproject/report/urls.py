
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_view, name='report_view'),  # Routes /report/ to the report_view
]
