from django.shortcuts import get_object_or_404, redirect, render
from website.models import Bank, BankBranch
from rest_framework import viewsets
from .serializers import BankSerializer, BankBranchSerializer

# from django.http import HttpRequest, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

from django.http import JsonResponse

class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Bank.objects.all().order_by('name')
    serializer_class = BankSerializer


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

# Create your views here.
# @csrf_exempt
def sayHi(request):
    # j = json.loads(request.body)
    # x = {  "fulfillmentText": "Hey! How are you doing?"
    #     }
    # return HttpResponse(json.dumps(x))
    # return HttpResponse('Works like a charm!')
    return JsonResponse({"fulfillmentText": "Hey! How are you doing?"})

    # Sample JSON RETURN
    # {
        # "fulfillmentText": "This is a text response",
        # "fulfillmentMessages": [
        # {
        #     "card": {
        #     "title": "card title",
        #     "subtitle": "card text",
        #     "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
        #     "buttons": [
        #         {
        #         "text": "button text",
        #         "postback": "https://assistant.google.com/"
        #         }
        #     ]
        #     }
        # }
        # ],
        # "source": "example.com",
        # "payload": {
        # "google": {
        #     "expectUserResponse": true,
        #     "richResponse": {
        #     "items": [
        #         {
        #         "simpleResponse": {
        #             "textToSpeech": "this is a simple response"
        #         }
        #         }
        #     ]
        #     }
        # },
        # "facebook": {
        #     "text": "Hello, Facebook!"
        # },
        # "slack": {
        #     "text": "This is a text response for Slack."
        # }
        # },
        # "outputContexts": [
        # {
        #     "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
        #     "lifespanCount": 5,
        #     "parameters": {
        #     "param": "param value"
        #     }
        # }
        # ],
        # "followupEventInput": {
        # "name": "event name",
        # "languageCode": "en-US",
        # "parameters": {
        #     "param": "param value"
        # }
        # }
    # }
