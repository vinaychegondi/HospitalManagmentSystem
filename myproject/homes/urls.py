from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Root URL for the home page
]
