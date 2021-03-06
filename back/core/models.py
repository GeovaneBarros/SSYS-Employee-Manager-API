from tabnanny import verbose
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    department = models.CharField(max_length=128)
    salary = models.FloatField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return f'{self.name} {self.department}'