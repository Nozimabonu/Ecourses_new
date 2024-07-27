from django.db import models
from teacher.models import Teacher


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    num_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    video = models.FileField(upload_to='videos/')
    teachers = models.ManyToManyField(Teacher)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def total_time(self):
        return self.duration / 60

    def __str__(self):
        return self.name


class Comments(models.Model):
    pass
