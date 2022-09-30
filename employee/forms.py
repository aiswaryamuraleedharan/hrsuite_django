from dataclasses import fields
from django.forms import ModelForm
from .models import EmployeeDetails

class EmployeeDetailsForm(ModelForm):
    class Meta:
        model=EmployeeDetails
        fields = ['name', 'reason', 'start_date', 'end_date']
 