from django.contrib import admin

# Register your models here.
from .models import Bank, BankBranch

admin.site.register(Bank)
admin.site.register(BankBranch)