from django.contrib import admin
from .models import student_Details

@admin.register(student_Details)
class student_list(admin.ModelAdmin):
    list_display = ('student_Name','student_Address','student_Dob','student_Father_Name','student_Image','student_Description')
