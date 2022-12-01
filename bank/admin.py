from django.contrib import admin

from bank.models import Account, Address, Card, Client, Imagem, Invoice, Loan, LoanPayment, Statement, Transfer, User

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Statement)
admin.site.register(Card)
admin.site.register(Invoice)
admin.site.register(Loan)
admin.site.register(LoanPayment)
admin.site.register(Imagem)