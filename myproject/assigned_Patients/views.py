from django.shortcuts import render
from django.db import connection


# Create your views here.
def assigned_patients(request):
    if request.method == 'POST':
        doctor_id = request.POST['DoctorID']

        with connection.cursor() as cursor:
            cursor.execute("select * from PatientDetails where Assigned_DocterID = (%s)", [doctor_id])

            colms = [column[0] for column in cursor.description]

            details = []
            for row in cursor.fetchall():
                details.append(dict(zip(colms, row)))

        return render(request, 'assigned_Patients.html', {'dic': details})

    else:
        return render(request, 'assigned.html')