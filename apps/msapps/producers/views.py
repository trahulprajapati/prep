from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
import logging
logger = logging.getLogger()

def hello(request):
    logger.log(msg='imjjjjj=====222', level=3)
    return HttpResponse('<h1> Resposnee revieved</h1>')

# Create your views here.
