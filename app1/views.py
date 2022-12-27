from django.shortcuts import render, redirect
from app1.models import Employee
from app1.forms import EmployeeForm
# Create your views here.


def home_view(request):
	employee=Employee.objects.all()
	return render(request,'app1/home.html',{'e':employee})


def insert_view(request):
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')
	return render(request,'app1/insert.html',{'form':form})


def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/home')


def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
			return redirect('/home')
	return render(request,'app1/update.html',{'employee':employee})

