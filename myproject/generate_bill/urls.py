
from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_bill, name='generate_bill'),  # Routes /billing/ to the generate_bill view
]
