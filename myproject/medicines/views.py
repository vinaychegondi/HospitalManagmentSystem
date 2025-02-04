from django.shortcuts import render
from django.db import connection

def prescription_view(request):
    if request.method == 'POST':
        patient_id = request.POST['Patient_ID']
        item_id = request.POST['Item_Number']

        with connection.cursor() as curs:
            # Check if the selected ItemID exists in medicines_list before inserting
            curs.execute("SELECT COUNT(*) FROM medicines_list WHERE ItemID = %s", [item_id])
            if curs.fetchone()[0] == 0:
                error_message = "Selected item does not exist in the medicines list."
                return render(request, 'medicines_form.html', {'error': error_message, 'dic': []})

            # ItemID exists, proceed to insert into prescription
            curs.execute("INSERT INTO Prescription (Patient_ID, Idem_ID) VALUES (%s, %s)", [patient_id, item_id])
        return render(request, 'prescription_success.html')

    else:
        # Fetch available Item_IDs and names for the dropdown and all details for the table
        with connection.cursor() as cursor:
            cursor.execute("SELECT ItemID, Medicine_Name, Company_Name, Dose, Price FROM medicines_list")
            medicines = cursor.fetchall()
            available_medicines = [{'ItemID': med[0], 'Medicine_Name': med[1], 'Company_Name': med[2], 'Dose': med[3], 'Price': med[4]} for med in medicines]

        return render(request, 'medicines_form.html', {'medicines': available_medicines, 'dic': available_medicines})
