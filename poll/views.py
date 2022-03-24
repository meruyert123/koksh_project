from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def iambest(request):
    return HttpResponse('HELLO')

def didi(request):
    print('fifa')


def hello():
    print('hello world')
    
