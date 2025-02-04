from django.shortcuts import render
from django.db import connection


# Create your views here.
def department_view(request):
    with connection.cursor() as cur:
        cur.execute("select * from Doctors_Details")
        columns = [column[0] for column in cur.description]

        data = []
        for row in cur.fetchall():
            data.append(dict(zip(columns, row)))

    return render(request, 'doctor.html', {'dic': data})