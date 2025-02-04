from django.shortcuts import render, redirect
from django.db import connection

def room_allotment(request):
    if request.method == 'POST':
        room_id = request.POST['Room_ID']
        patient_id = request.POST['Patient_ID']

        with connection.cursor() as exe:
            # Insert the new room allotment
            exe.execute("INSERT INTO Room (RoomID, Patient_ID) VALUES (%s, %s)", [room_id, patient_id])

        return redirect('/home/')  # Adjust the redirect URL as needed

    else:
        with connection.cursor() as cursor:
            # Fetch available rooms (rooms not assigned to any patient)
            cursor.execute("SELECT * FROM RoomDetails WHERE RoomType NOT IN (SELECT RoomID FROM Room)")
            available_columns = [col[0] for col in cursor.description]
            available_rooms = [dict(zip(available_columns, row)) for row in cursor.fetchall()]

            # Fetch booked rooms with patient details
            cursor.execute("""
                SELECT r.RoomID, rd.Room_Description, rd.Cost, p.PatientID, p.First_Name, p.Last_Name
                FROM Room r
                INNER JOIN RoomDetails rd ON r.RoomID = rd.RoomType
                INNER JOIN PatientDetails p ON r.Patient_ID = p.PatientID
            """)
            booked_columns = [col[0] for col in cursor.description]
            booked_rooms = [dict(zip(booked_columns, row)) for row in cursor.fetchall()]

        return render(request, 'room_allotment_form.html', {
            'available_rooms': available_rooms,
            'booked_rooms': booked_rooms
        })
