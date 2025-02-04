from django.shortcuts import render
from django.db import connection

def report_view(request):
    if request.method == 'POST':
        patient_id = request.POST['Patient_ID']
        report_type = request.POST['Report_Type']

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO TestReports(Patient_ID, ReportType) VALUES (%s, %s)", [patient_id, report_type])

        return render(request, 'reportsucess.html')

    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Report_Type FROM Reports")
            report_types = [row[0] for row in cursor.fetchall()]

            cursor.execute("SELECT * FROM Reports")
            attr = [column[0] for column in cursor.description]
            details = [dict(zip(attr, row)) for row in cursor.fetchall()]

        return render(request, 'reportform.html', {'dic': details, 'report_types': report_types})
