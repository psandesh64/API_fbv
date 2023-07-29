from rest_framework import serializers
from app1 import models
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        # fields = ['name','email']
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
