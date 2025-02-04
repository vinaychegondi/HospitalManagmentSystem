from django.shortcuts import render

# Create your views here.
def report_medicines(request):
    return render(request, 'report_medicines.html')