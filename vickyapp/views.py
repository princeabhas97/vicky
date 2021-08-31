from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import vickytest

@api_view(['POST'])
def vicky_views(request):
    print('this is a request',request.data)
    firstname=request.data['firstname']
    lastname = request.data['lastname']
    email = request.data['email']
    saction=request.data['saction']
    emp=vickytest.objects.create(
        firstname=firstname,
        lastname=lastname,
        email=email,
        saction=saction,
    )
    return Response({"message": "this is test response of abhas project"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_views2(request, standard=None):
   # print('this is a request',request.data)
    firstname=request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    email = request.GET.get('email')
    saction = request.GET.get('saction')
    emp=vickytest.objects.create(
        firstname=firstname,
        lastname=lastname,
        email=email,
   saction = saction,
    )
    return Response({"message": "this is test response of abhas project"}, status=status.HTTP_200_OK)