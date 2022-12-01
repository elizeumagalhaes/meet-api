from django.urls import path
from .views import *
from rest_framework_nested import routers

rota = routers.DefaultRouter()
rota.register('usuarios', UserViewSet, basename='usuarios')
rota.register('contas', AccountViewSet, basename='contas')
rota.register('cartoes', CardViewSet, basename='cartoes')
rota.register('faturas', InvoiceViewSet, basename='faturas')
rota.register('clientes', ClientViewSet, basename='clientes')
rota.register('enderecos', AddressViewSet, basename='enderecos')
rota.register('transferencias', TransferViewSet, basename='transferencias')
rota.register('extratos', StatementViewSet, basename='extratos')
rota.register('emprestimos', LoanViewSet, basename='emprestimos')
rota.register('pgt_emprestimos', LoanPaymentViewSet, basename='emprestimos')
rota.register('imagens', ImagemViewSet, basename='imagens')
rota.register('adicionar-imagens', AddImagemViewSet, basename='adicionar-imagens')

urlpatterns = rota.urls