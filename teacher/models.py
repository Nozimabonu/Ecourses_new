from django.db import models
from courses.models import Courses

# Create your models here.

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    imag = models.ImageField()
    description = models.TextField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)