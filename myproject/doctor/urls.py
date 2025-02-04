from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_view, name='department'),  # Use `department_view` here
]
