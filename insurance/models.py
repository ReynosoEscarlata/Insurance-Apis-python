from django.db import models

# Create your models here.

class Vehicle(models.Model):
    brand = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=50, null=False)
    year = models.CharField(max_length=4, null=False)
    serial_number = models.CharField(max_length=100, null=False)
    class Meta:
        managed = True
        db_table = 'insurance_vehicle'

class Driver(models.Model):
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.TextField(max_length=50, null=False)
    address = models.TextField(max_length=100, null=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    class Meta:
        managed = True
        db_table = 'insurance_driver'


class InsuranceApplication(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    active_status = models.CharField(max_length=15, null=False, default="Submission")

    class Meta:
        managed = True
        db_table = 'insurance_application'

class InsuranceStatus(models.Model):
    INSURANCE_STATUS=[
        ('SUBMISSION','Submission'),
        ('REVIEW','Review'),
        ('APPROVAL','Approval'),
        ('REJECTION','Rejection')
        ]
    status = models.CharField(max_length=15,null=False, choices=INSURANCE_STATUS)
    date = models.DateTimeField(null=False)
    insurance_application = models.ForeignKey(InsuranceApplication, on_delete=models.DO_NOTHING, null=True)
    class Meta:
        managed = True
        db_table = 'insurance_status'


