from django.shortcuts import render
from django.db import connection


# Create your views here.
def patient_view(request):
    if request.method == 'POST':

        firstname = request.POST['First_Name']
        lastname = request.POST['Last_Name']
        age = request.POST['Age']
        symptoms = request.POST['Symptoms']
        patient_address = request.POST['Patient_Address']
        gender = request.POST['Gender']
        phone = request.POST['Phone']
        admit_date = request.POST['Admit_date']
        assigned_doctor_id = request.POST['Assigned_DoctorID']

        with connection.cursor() as exe:
            exe.execute("insert into PatientDetails(First_Name, Last_Name, Age, Symptoms, Patinet_Address, Gender, Phone, Admitdate, Assigned_DocterID) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", [firstname, lastname, age, symptoms, patient_address, gender, phone, admit_date, assigned_doctor_id],)



        return render(request, 'Patient Sucess.html', {'dict': firstname})
    else:
        return render(request, 'patient.html')