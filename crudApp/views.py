from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            # print("nikAdd")
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            newEmployee = Employee(id=id,name=name,email=email,address=address,phone=phone)
            newEmployee.save()
        elif 'edit' in request.POST:
            # print("nikEdit")
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            editEmployee = Employee.objects.get(id=id)
            editEmployee.name = name
            editEmployee.email = email
            editEmployee.address = address
            editEmployee.phone = phone
            editEmployee.save()
        elif 'delete' in request.POST:
            # print("nikDelete")
            id = request.POST['id']
            deleteEmployee = Employee.objects.get(id=id)
            deleteEmployee.delete()

    
    employee = Employee.objects.all()
    context = {
        'employee' : employee
    }
    print(employee)
    return render(request,"index.html",context)
