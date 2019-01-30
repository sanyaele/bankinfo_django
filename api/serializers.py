from website.models import Bank, BankBranch
from rest_framework import serializers

class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ('url', 'name', 'ussd', 'website')

class BankBranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankBranch
        fields = ('url', 'branch', 'lon_lat')