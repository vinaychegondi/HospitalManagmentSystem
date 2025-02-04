from django.shortcuts import render
from django.db import connection

def generate_bill(request):
    if request.method == 'POST':
        patient_id = int(request.POST['PatientID'])

        try:
            with connection.cursor() as cursor:
                # Call SP_F_Bill to populate the bill
                cursor.callproc('SP_F_Bill', [patient_id])

                # Fetch the bill summary
                cursor.execute('''
                    SELECT 
                        Patient_ID, 
                        SUM(RoomCharges) AS Total_Room_Charges, 
                        SUM(Reports_Charges) AS Total_Report_Charges, 
                        SUM(Medicines_fee) AS Total_Medicine_Fee,
                        SUM(Total_Due) AS Total_Due_Amount
                    FROM bill
                    WHERE Patient_ID = %s
                    GROUP BY Patient_ID
                ''', [patient_id])

                columns = [col[0] for col in cursor.description]
                details = [dict(zip(columns, row)) for row in cursor.fetchall()]

                if not details:
                    return render(request, 'error.html', {'message': 'No bill generated for this patient.'})

        except Exception as e:
            return render(request, 'error.html', {'message': f"Error: {e}"})

        return render(request, 'Bill_Summary.html', {'bill_summary': details})

    return render(request, 'generate_form.html')
