from django.db import models

# Represents a company
class Company(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


# Represents an employee
class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Represents a device
class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # New field for price


    def __str__(self):
        return self.name


# Represents a log entry for a device
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_date = models.DateField()
    checked_in_date = models.DateField()

    def __str__(self):
        return f"{self.device.name} - Log ID: {self.id}"