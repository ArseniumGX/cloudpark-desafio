from django.contrib import admin
from .models import (Contract, ContractRule, Customer, CustomerPlan, ParkMovement, Plan, Vehicle)
# Register your models here.

admin.site.register(Contract)
admin.site.register(ContractRule)
admin.site.register(Customer)
admin.site.register(CustomerPlan)
admin.site.register(ParkMovement)
admin.site.register(Plan)
admin.site.register(Vehicle)