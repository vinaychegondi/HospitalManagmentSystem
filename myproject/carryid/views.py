from django.shortcuts import render

# Create your views here.
def carryid(request):
    if request.method == 'POST':
        x = str(request.body)

        print(x)

    return render(request, 'patient_id.html')
