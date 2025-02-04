# Pat_Test_Details/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pat_test_view, name='pat_test_view'),  # Routes /pat_test/ to the pat_test_view
]
