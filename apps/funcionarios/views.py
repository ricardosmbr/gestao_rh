from django.http import HttpResponse
from django.shortcuts import render

def funcionario(request):
    return HttpResponse("ola Mundo")
