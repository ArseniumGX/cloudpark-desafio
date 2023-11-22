from django.urls import path
from .views import (CustomerAPIView, VehicleAPIView, PlanAPIView, CustomerPlanAPIView, ContractAPIView, ContractRuleAPIView, ParkMovementAPIView)

urlpatterns = [
   path('customer', CustomerAPIView.as_view()),
   path('customer/<int:pk>', CustomerAPIView.as_view()),
   path('vehicle', VehicleAPIView.as_view()),
   path('vehicle/<int:pk>', VehicleAPIView.as_view()),
   path('plan', PlanAPIView.as_view()),
   path('plan/<int:pk>', PlanAPIView.as_view()),
   path('customerplan', CustomerPlanAPIView.as_view()),
   path('customerplan/<int:pk>', CustomerPlanAPIView.as_view()),
   path('contract', ContractAPIView.as_view()),
   path('contract/<int:pk>', ContractAPIView.as_view()),
   path('contractrule', ContractRuleAPIView.as_view()),
   path('contractrule/<int:pk>', ContractRuleAPIView.as_view()),
   path('parkmoviment', ParkMovementAPIView.as_view()),
   path('parkmoviment/<int:pk>', ParkMovementAPIView.as_view()),
]