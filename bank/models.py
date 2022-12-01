from unicodedata import name
from django.db import models
from pictures.models import PictureField

class User(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.cpf

class Client(models.Model):

    basic = 'G'
    premium = 'P'
    prime = 'B'

    types = [
        (basic, 'Gold'),
        (premium, 'Platinum'),
        (prime, 'Black'),
    ]

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=20)
    birth_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=types, default=basic)

    def __str__(self) -> str:
        return self.name

class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    cep = models.CharField(max_length=8)

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='client')
    agency = models.CharField(max_length=4, verbose_name='agency')
    account = models.CharField(max_length=9, unique=True, verbose_name='account')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='balance')

    def __str__(self):
        return str(self.client)

class Transfer(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='sender')
    recipient = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='recipient')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender + " " + self.recipient

class Statement(models.Model):
    transfer = 'T'
    deposit = 'D'
    withdrawal = 'W'
    loan = 'L'

    operations = [
        (transfer, 'Transfer'),
        (deposit, 'Deposit'),
        (withdrawal, 'Withdrawal'),
        (loan, 'Loan'),
    ]

    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    operation = models.CharField(max_length=1, choices=operations)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField()

class Card(models.Model):
    virtual = 'V'
    physical = 'F'

    types = [
        (virtual, 'Virtual'),
        (physical, 'Físico'),
    ]

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    number = models.CharField(max_length=16, unique=True)
    cvv = models.CharField(max_length=3)
    validty = models.DateField()
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=1, choices=types, default=physical)
    flag = models.CharField(max_length=20)
    ative = models.BooleanField()
    due_date = models.DateField()

class Invoice(models.Model):
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Loan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    approved = models.BooleanField()
    instalments = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    first_installment = models.DateField()
    up_to_date = models.BooleanField()
    installments_paid = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Imagem(models.Model):
    title = models.CharField(max_length=255)
    photo = PictureField(upload_to='loja/imagens')