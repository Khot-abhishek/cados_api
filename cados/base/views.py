from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def endpoint(request):
    data = ['endpoint', 'endpoint:username']
    return JsonResponse(data, safe=False)