from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            # print("nikAdd")
            checkbox = 0
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            newEmployee = Employee(checkbox=checkbox,name=name,email=email,address=address,phone=phone)
            newEmployee.save()
        elif 'edit' in request.POST:
            # print("nikEdit")
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            editEmployee = Employee.objects.filter(id=id)
            editEmployee.name = name
            editEmployee.email = email
            editEmployee.address = address
            editEmployee.phone = phone
            editEmployee.save()
        elif 'delete' in request.POST:
            # print("nikDelete")
            id = request.POST['id']
            deleteEmployee = Employee.objects.filter(id=id)
            deleteEmployee.delete()
        elif 'deleteAll' in request.POST:
            checkedEmployee = Employee.objects.filter(checkbox=1)
            print(checkedEmployee)
            for emp in checkedEmployee:
                emp.delete()

    
    employee = Employee.objects.all()
    count = Employee.objects.count()
    context = {
        'employee' : employee,
        'count': count
    }
    return render(request,"index.html",context)
