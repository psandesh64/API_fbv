from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    Subject = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.name}'

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
