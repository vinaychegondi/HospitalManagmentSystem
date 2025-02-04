from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.assigned_patients, name='assigned_patients'),  # Routes /assigned/ to this view
        path('report_medicines/', include('report_medicines.urls')),  # Nested URL for report_medicines under assigned
]
