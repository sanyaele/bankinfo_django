from django.db import models
# from django.utils import timezone

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    synonyms = models.CharField(max_length=250, null=True, blank=True)
    ussd = models.CharField(max_length=6, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    other_websites = models.CharField(max_length=250, null=True, blank=True)
    phone_numbers = models.CharField(max_length=250, null=True, blank=True)
    email_addresses = models.CharField(max_length=500, null=True, blank=True)
    countryTLD = models.CharField(max_length=2, default="NG")

class BankBranch(models.Model):
    Bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    Branch = models.CharField(max_length=100, null=True, blank=True)
    lon_lat = models.CharField(max_length=100, null=True, blank=True)
    ATM = models.BooleanField(default=False)
