from rest_framework.serializers import ModelSerializer
from bank.models import Account, Card, Imagem, Invoice, Loan, LoanPayment, Statement, Transfer, User, Client, Address
from pictures.contrib.rest_framework import PictureField

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'cpf', 'password']

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'last_name', 'email', 'phone_number', 'gender', 'birth_date', 'user', 'type']

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['client', 'state', 'city', 'district', 'street', 'number', 'cep']

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'client', 'agency', 'account', 'balance']

class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'sender', 'recipient', 'value', 'date_time']

class StatementSerializer(ModelSerializer):
    class Meta:
        model = Statement
        fields = ['id', 'account', 'operation', 'value', 'date_time']

class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'client', 'number', 'cvv', 'validty', 'limit', 'type', 'flag', 'ative', 'due_date']

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'card', 'value', 'date']

class LoanSerialier(ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'account', 'value', 'date', 'interest_rate', 'approved', 'instalments', 'amount', 'first_installment', 'up_to_date', 'installments_paid', 'amount_paid']

class LoanPaymentSerializer(ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = ['id', 'loan', 'value', 'date']

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'title', 'photo']
    photo = PictureField()

class AddImageSerializer(ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'title', 'photo']
