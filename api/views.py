from django.shortcuts import render
from django.http import JsonResponse
from .models import Countries
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return None

@csrf_exempt
def country(request):
    if request.method == 'POST':
        return JsonResponse(Countries.objects.all(), safe=False)

@csrf_exempt
def state(request):
    pass

@csrf_exempt
def city(request):
    pass