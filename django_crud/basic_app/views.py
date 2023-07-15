from django.shortcuts import render,redirect
from .models import Position, Employee
from .forms import EmployeeForm


# Create your views here.
def index(request):
    return render(request, 'basic_app/base.html')

def Employee_list(request):
    emps = Employee.objects.all()
    return render(request, 'basic_app/Employee_list.html',{'emps':emps})

def Employee_form(request,id=0):
    if request.method == 'POST':
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form = form.save()
            return redirect(Employee_list)
    elif request.method=='GET':
        if id==0:
            form = EmployeeForm()
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)
        return render(request, 'basic_app/Employee_form.html',{'form':form})


def Employee_delete(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect(Employee_list) 