from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from docman.models import DocumentType
from docman.serializers import DocumentTypeSerializer

@csrf_exempt
def welcome(request):
    return JsonResponse(dict(message="Welcome to Document Management System"), status=200, safe=False)