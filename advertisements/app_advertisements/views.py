from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Успешно, главная стр')

def page1(request):
    return HttpResponse('Успешно, usual стр')
# Create your views here.
