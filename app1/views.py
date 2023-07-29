from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from app1 import models
from app1.serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def home_page(request):
    return render(request,'index.html')

@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        Employee = models.Employee.objects.all()
        serializer = EmployeeSerializer(Employee,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=jsonData)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

@csrf_exempt       
def employeeDetailView(request,pk):
    try:
        employee = models.Employee.objects.get(pk=pk)
        # return JsonResponse('employee'+ str(pk), safe=False)
    except models.Employee.DoesNotExist:
        return HttpResponse(status=404)
    print(employee)
    if request.method=='DELETE':
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='PUT':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
    # return JsonResponse('hello',safe=False)

def userListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return JsonResponse(serializer.data,safe=False)