from django.shortcuts import render
from django.db import connection

def pat_prescription_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT PatientID, First_Name, Last_Name, Age, Gender, Medicine_Name, Company_Name, Dose, Price FROM Patient_Medicine")
        columns = [column[0] for column in cursor.description]

        content = []
        for row in cursor.fetchall():
            content.append(dict(zip(columns, row)))

    # Print the data to debug and ensure Price values are included
    #print("Data sent to template:", content)

    return render(request, 'pat_prescription.html', {'list': content})
