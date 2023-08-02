from django.shortcuts import render
from .models import Employee
import uuid

# Create your views here.
def index(request):
    print("nikPOST")
    if request.method == 'POST':
        if 'add' in request.POST:
            # print("nikAdd")
            id = str(uuid.uuid4())[:7]
            checkbox = False
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            newEmployee = Employee(id=id,checkbox=checkbox,name=name,email=email,address=address,phone=phone)
            newEmployee.save()
        elif 'edit' in request.POST:
            # print("nikEdit")
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            editEmployee = Employee.objects.filter(id=id)
            for emp in editEmployee:
                emp.name = name
                emp.email = email
                emp.address = address
                emp.phone = phone
                emp.save()
        elif 'delete' in request.POST:
            # print("nikDelete")
            id = request.POST['id']
            deleteEmployee = Employee.objects.filter(id=id)
            for emp in deleteEmployee:
                emp.delete()
        elif 'deleteAll' in request.POST:
            # print("nikDeleteAll")
            checkedEmployee = Employee.objects.filter(checkbox=True)
            for emp in checkedEmployee:
                # print("nikDeleteAll..")
                emp.delete()
        else:
            # print("nikElse")
            checkbox_value = request.POST['checkbox_value']
            # print(checkbox_value)
            id = request.POST['value']
            # print(id)
            checkedEmployee = Employee.objects.filter(id=id)
            # print(checkedEmployee)
            for emp in checkedEmployee:
                # print("nikForLoop")
                if checkbox_value=="true":
                    emp.checkbox = True
                    # print("nikTrue")
                elif checkbox_value=="false":
                    # print("nikFalse")
                    emp.checkbox = False
                else:
                    # print("nikLast")
                    print(emp.checkbox)
                emp.save()

    count = Employee.objects.count()
    employee = Employee.objects.all()
    context = {
        'employee' : employee,
        'count':count
    }
    # for emp in employee:
    #     print(emp.checkbox,type(emp.checkbox))
    return render(request,"index.html",context)
