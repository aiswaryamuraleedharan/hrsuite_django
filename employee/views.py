from django.shortcuts import render,redirect
from .forms import EmployeeDetailsForm
from .models import EmployeeDetails

def Home(request):
    data=EmployeeDetails.objects.all()
    return render(request,'register.html',{'data1':data})

def Employee(request):
    form=EmployeeDetailsForm()
    context={'form':form}
    if request.method == 'POST':
        form1 = EmployeeDetailsForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,'employee.html',context)

def Update(request,pk):
    data = EmployeeDetails.objects.get(id=pk)
    form = EmployeeDetailsForm(instance=data)
    context={'form':form}
    if request.method == 'POST':
        form1= EmployeeDetailsForm(request.POST,instance=data)
        if form1.is_valid(): 
            form1.save()
            return redirect('/')
    return render(request,'employee.html',context)

def DeleteUser(request,pk):
    data = EmployeeDetails.objects.get(id=pk)
    data.delete()
    return redirect('home')
