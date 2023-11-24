from django.urls import path
from .views import (ContractAPIView)

urlpatterns = [
   # Para cadastro e edição de clientes
   # path('/customer'),
   # Para cadastro e edição de planos
   # path('/plan'),
   # Para cadastro e edição de veículos
   # path('/vehicle'),
   # Para cadastro e edição de contratos
   path('contract', ContractAPIView.as_view()),
   # Para cadastro de veículos (vincular vehicle/custumer)
   # path('/customervehicle'),
   # Para efetuar o vínculo do plano com o cliente
   # path('/customerplan'), 
   # Para dar entrada/saída em movimentos do pátio
   # path('parkmoviment')
]