from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,'principal.html')
def student(request):
    return render(request,'student.html')

def principal2(request):
    return render(request,'principal2.html')