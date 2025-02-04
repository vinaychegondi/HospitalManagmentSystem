from django.shortcuts import render
from django.db import connection

def see_bill_view(request):
    if request.method == 'POST':
        patient_id = request.POST['PatientID']

        with connection.cursor() as cursor:
            cursor.execute('SELECT Patient_ID, RoomCharges, Reports_Charges, Medicines_fee, Total_Due FROM bill WHERE Patient_ID = %s', [patient_id])
            columns = [column[0] for column in cursor.description]
            details = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Print details to verify data
        print("Bill Summary Data:", details)

        return render(request, 'see_bill.html', {'col': details})
    else:
        return render(request, 'see_form.html')
