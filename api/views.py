from django.shortcuts import render
from django.http import JsonResponse
from .models import Countries, States, Cities
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return None

@csrf_exempt
def country(request):
    if request.method == 'POST':
        return JsonResponse({
            'values': list(Countries.objects.all().values())
        }, safe=False)

@csrf_exempt
def state(request):
    if request.method == 'POST':
        country_id = request.POST.get('id')
        return JsonResponse({
            'values': list(States.objects.filter(country_id=country_id).values())
        }, safe=False)

@csrf_exempt
def city(request):
    if request.method == 'POST':
        state_id = request.POST.get('id')
        return JsonResponse({
            'values': list(Cities.objects.filter(state_id=state_id).values())
        }, safe=False)
