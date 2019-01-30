from django.shortcuts import get_object_or_404, redirect, render
from website.models import Bank, BankBranch
from rest_framework import viewsets
from .serializers import BankSerializer, BankBranchSerializer


class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Bank.objects.all().order_by('name')
    serializer_class = BankSerializer

# class SearchBankViewSet(viewsets.ModelViewSet):
#     # End point to search for a bank's information
#     def get(self, request):
#         bank = request.bank

#     queryset = Bank.objects.get(name=bank)
#     serializer_class = BankSerializer


class BankBranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows grobank branches to be viewed or edited.
    """
    queryset = BankBranch.objects.all()
    serializer_class = BankBranchSerializer

# # Create your views here.
def SearchBankView(request, bank_name):
    bankname = Bank.objects.get(name__icontains=bank_name)
    # bankname = get_object_or_404(Bank, name__icontains=bank_name)

    #hard code redirect
    direct_uri = ('/api/banks/' + str(bankname.id))
    return redirect(direct_uri)
    # return redirect('banks', pk=bankname.pk)
