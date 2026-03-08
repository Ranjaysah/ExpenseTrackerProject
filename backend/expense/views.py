from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
import json
from .models import *

# Create your views here.

#Singup API
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        fullname = data.get('Fullname')
        email = data.get('Email')
        password = data.get('Password')

        if UserDetail.objects.filter(Email = email).exists():
            return JsonResponse({'message':'Email already exists'}, status=400)
        UserDetail.objects.create(Fullname=fullname, Email=email, Password=password)
        return JsonResponse({'message':'User registered Successfully'}, status=201)
    


 




