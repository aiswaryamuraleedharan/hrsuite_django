from django.shortcuts import render,redirect
from employee.models import EmployeeDetails

def Home(request):
    data=EmployeeDetails.objects.all()
    return render(request,'index.html',{'data1':data})

def approve(request,pk):
    data=EmployeeDetails.objects.get(id=pk)
    data.status=1
    data.save()
    return redirect('home')

def reject(request,pk):
    data=EmployeeDetails.objects.get(id=pk)
    data.status=2
    data.save()
    return redirect('home')
   
   