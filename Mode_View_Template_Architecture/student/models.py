from django.db import models
from django.utils import timezone

class student_Details(models.Model):
    student_Name = models.CharField(max_length=50)
    student_Address = models.CharField(max_length=100)
    student_Dob = models.DateTimeField(timezone.now)
    student_Father_Name = models.CharField(max_length=50)
    student_Image = models.ImageField(upload_to = 'image/')
    student_Description = models.TextField(default = '')
    
