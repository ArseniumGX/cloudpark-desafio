from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    card_id = models.CharField(max_length=10, unique=True)

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=50, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, unique=True)
    value = models.FloatField()

class CustomerPlan(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True)

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, unique=True)
    max_value = models.FloatField(null=True)

class ContractRule(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, )
    until = models.IntegerField()
    value = models.FloatField()

class ParkMovement(models.Model):
    id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    value = models.FloatField(null=True)
