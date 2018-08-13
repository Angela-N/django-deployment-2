from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=254)
    principal = models.CharField(max_length=254)
    motto = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name