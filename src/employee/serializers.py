from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'role', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def validate_email(self, value: str):
        #check if an employee already exist with this email

        if self.instance:   
            if Employee.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
                raise serializers.ValidationError(f"Employee with this email {value} alreadry exists")
        else:
            if Employee.objects.filter(email=value).exists():
                raise serializers.ValidationError(f"Employee withis email {value} already exists")
        return value.lower()
    
    def validate_name(self, value: str):
        if not value or not value.strip():
            raise serializers.ValidationError("Name can not be empty")
        return value.strip()
    
    def validate(self, attrs):
        return attrs
