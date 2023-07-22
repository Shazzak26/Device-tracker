from django.urls import path
from .views import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateDestroyAPIView,
    EmployeeListCreateAPIView,
    EmployeeRetrieveUpdateDestroyAPIView,
    DeviceListCreateAPIView,
    DeviceRetrieveUpdateDestroyAPIView,
    DeviceLogListCreateAPIView,
    DeviceLogRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Company URLs
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    # Represents the endpoint for listing and creating companies
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-retrieve-update-destroy'),
    # Represents the endpoint for retrieving, updating, and deleting a specific company
    
    # Employee URLs
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    # Represents the endpoint for listing and creating employees
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    # Represents the endpoint for retrieving, updating, and deleting a specific employee
    
    # Device URLs
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    # Represents the endpoint for listing and creating devices
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrieve-update-destroy'),
    # Represents the endpoint for retrieving, updating, and deleting a specific device
    
    # Device Log URLs
    path('devicelogs/', DeviceLogListCreateAPIView.as_view(), name='devicelog-list-create'),
    # Represents the endpoint for listing and creating device logs
    path('devicelogs/<int:pk>/', DeviceLogRetrieveUpdateDestroyAPIView.as_view(), name='devicelog-retrieve-update-destroy'),
    # Represents the endpoint for retrieving, updating, and deleting a specific device log
]