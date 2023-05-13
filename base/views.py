from django.shortcuts import render
from django.http import HttpResponse


def getResponse(request):
    return HttpResponse("<h1>Hello there! hello world!!</h1>")