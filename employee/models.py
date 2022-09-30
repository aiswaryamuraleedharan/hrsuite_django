from django.db import models

class EmployeeDetails(models.Model):
    name=models.CharField(max_length=25)
    reason=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name 