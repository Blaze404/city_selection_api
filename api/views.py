from django.shortcuts import render
from django.http import JsonResponse
from .models import Countries

# Create your views here.
def index(request):
    return None


def country(request):
    if request.method == 'POST':
        return JsonResponse(Countries.objects.all())

def state(request):
    pass

def city(request):
    pass