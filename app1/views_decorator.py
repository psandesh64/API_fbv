from django.shortcuts import render
from app1 import models
from django.http import JsonResponse
from app1.serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def home_page(request):
    return render(request,'index.html')

@api_view(['GET','POST'])
def employeeListView(request):
    if request.method == 'GET':
        Employee = models.Employee.objects.all()
        serializer = EmployeeSerializer(Employee,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE','GET','POST'])     
def employeeDetailView(request,pk):
    try:
        employee = models.Employee.objects.get(pk=pk)
        # return JsonResponse('employee'+ str(pk), safe=False)
    except models.Employee.DoesNotExist:
        return Response(status=404)
    print(employee)
    if request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    # return JsonResponse('hello',safe=False)

@api_view(['GET'])
def userListView(request):
    if request.method=='GET':
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)