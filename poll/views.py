from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def iambest(request):
    return HttpResponse('HELLO')

def didi(request):
    print('fifa')

    
