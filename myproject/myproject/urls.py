"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from medicines import views as medicines_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("homes.urls")),  # Root URL for `homes` app
        path('doctor/', include('doctor.urls')),
            path('assigned/', include('assigned_Patients.urls')),
            path('patient/', include('patient.urls')),
                path('carryid/', include('carryid.urls')),
        path('generate_bill/', include('generate_bill.urls')),
            path('report_medicines/', include('report_medicines.urls')),
                path('report_form/', include('report.urls')),
                    path('Pat_Prescription/', include('Pat_Prescription_Details.urls')),
                        path('medicines/', include('medicines.urls')),
                            path('Pat_test/', include('Pat_Test_Details.urls')),
                                path('room_allocation/', include('Room_allotment.urls')),
                                    path('see_bill/', include('see_bill.urls')),
                                                                        path('prescription/', medicines_views.prescription_view, name='prescription'),
        path('services/', include('services.urls')),
        path('contact/', include('contact.urls')),   # Direct URL for prescription

]
