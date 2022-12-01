import decimal
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import *
from bank.models import Account, Imagem, Invoice, Loan, LoanPayment, Statement, Transfer, User, Client, Address, Card
from bank.serializer import AccountSerializer, AddImageSerializer, AddressSerializer, CardSerializer, ClientSerializer, ImageSerializer, InvoiceSerializer, LoanPaymentSerializer, LoanSerialier, StatementSerializer, TransferSerializer, UserSerializer

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):


        return super().create(request, *args, **kwargs)

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def create(self, request, *args, **kwargs):
        sender = Account.objects.get(pk=self.request.data['sender'])
        recipient = Account.objects.get(pk=self.request.data['recipient'])
        value = decimal.Decimal(self.request.data['value'])

        if sender.balance >= value:
            updatedSenderBalance = sender.balance - value
            updatedRecipientBalance = recipient.balance + value
            object_sender = {'client':sender.client.pk, 'agency':sender.agency, 'account':sender.account, 'balance':updatedSenderBalance}
            object_recipient = {'client':recipient.client.pk, 'agency':recipient.agency, 'account':recipient.account, 'balance':updatedRecipientBalance}

            serializer_sender = AccountSerializer(sender, data=object_sender)
            serializer_recipient = AccountSerializer(recipient, data=object_recipient)

            if serializer_sender.is_valid() and serializer_recipient.is_valid():
                serializer_sender.save()
                serializer_recipient.save()
            else:
                print(serializer_sender.errors)
        return super().create(request, *args, **kwargs)

class StatementViewSet(ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerialier

class LoanPaymentViewSet(ModelViewSet):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer

class ImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImageSerializer

class AddImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = AddImageSerializer