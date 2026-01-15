from rest_framework import status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee CRUD operations.
    
    Provides:
    - List all employees (GET /api/employees/)
    - Create employee (POST /api/employees/)
    - Retrieve employee (GET /api/employees/{id}/)
    - Update employee (PUT /api/employees/{id}/)
    - Delete employee (DELETE /api/employees/{id}/)
    
    Features:
    - Filtering by department and role
    - Pagination (10 items per page)
    - JWT authentication required
    - Proper HTTP status codes
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Create a new employee.
        Returns 201 Created on success.
        Returns 400 Bad Request on validation errors.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    
    def list(self, request, *args, **kwargs):
        """
        List all employees with pagination and filtering.
        Returns 200 OK.
        """
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single employee.
        Returns 200 OK if found.
        Returns 404 Not Found if employee doesn't exist.
        """
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        Update an employee.
        Returns 200 OK on success.
        Returns 400 Bad Request on validation errors.
        Returns 404 Not Found if employee doesn't exist.
        """
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete an employee.
        Returns 204 No Content on success.
        Returns 404 Not Found if employee doesn't exist.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

