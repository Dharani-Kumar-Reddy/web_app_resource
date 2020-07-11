from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view

#for testing
@api_view(['GET'])
def test(request):
    
    th=requests.post('http://127.0.0.1:8000/login',params={'username':'uddin','password':'admin@123'})
    
    track_liv=th.json()
    print(track_liv)
    return JsonResponse(track_liv,safe=False)	