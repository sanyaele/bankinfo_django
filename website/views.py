from .models import Bank
from django.shortcuts import render, get_object_or_404


# Create your views here.
def bank_list(request):
    banks = Bank.objects.filter(countryTLD='NG').order_by('name')
    return render(request, 'website/index.html', {'banks': banks})

def bank_detail(request, pk):
    #bank = Bank.objects.get(pk=pk)
    bank = get_object_or_404(Bank, pk=pk)
    return render(request, 'website/bank_detail.html', {'bank': bank})