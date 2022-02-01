from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home')

def products(contact):
    return HttpResponse('products')

def customer(contact):
    return HttpResponse('customer')