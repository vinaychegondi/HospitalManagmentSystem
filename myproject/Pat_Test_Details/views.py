# Pat_Test_Details/views.py
from django.shortcuts import render
from django.db import connection

def pat_test_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Patient_Report")
        cur = [column[0] for column in cursor.description]

        context = []
        for row in cursor.fetchall():
            context.append(dict(zip(cur, row)))

    return render(request, 'pat_test_reports.html', {'tup': context})
