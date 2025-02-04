# see_bill/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.see_bill_view, name='see_bill_view'),  # Routes /see_bill/ to the see_bill_view
]
