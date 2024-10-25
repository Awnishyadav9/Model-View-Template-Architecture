from django.shortcuts import render
from .models import student_Details

def student(request):
    student_det = student_Details.objects.all()
    return render(request,'index.html',{'student_det':student_det})
