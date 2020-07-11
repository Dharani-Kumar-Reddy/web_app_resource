from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from .db import query
import json
import requests
from django.http import JsonResponse
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        status=request.POST.get('status')
        category=request.POST.get('category')
        print("fhief",username)
        try:
            x=query(f"""SELECT * FROM res.users WHERE user_name={username}""",return_json=False)
            if len(x)>0: return Response({"message":"A user with that user_id already exists."},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"There was an error inserting into users table."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            query(f"""INSERT INTO res.users (user_name, phone_num,email_id,password,category,status) VALUES (
            {username},{phone},{email},{password},{category},{status})""")
        except:
            return Response({"message":"There was an error inserting into users table."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message":"Successfully Inserted."},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def details(request):
    if request.method=='GET':
        return Response(query(f"""SELECT * FROM res.users """,return_json=False))
    



@api_view(['POST'])   
def Adminlogin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    print(password)
    user=User.getUserById(username)
    if user.status==1:
        if user and safe_str_cmp(user.password,password):
            access_token=create_access_token(identity=user.username,expires_delta=False)
            return Response({'access_token':access_token},status=status.HTTP_200_OK)
        return Response({"message":"Invalid Credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({"message":"Not an admin"}, status=status.HTTP_401_UNAUTHORIZED)


class User():
    def __init__(self,username,password,status):
        self.username=username
        self.password=password
        self.status=status
    @classmethod
    def getUserById(cls,username):
        result=query(f"""select user_name,password,status from res.users where user_name={username}""",return_json=False)
        if len(result)>0:
            return User(result[0]['user_name'],result[0]['password'],result[0]['status'])
        else:
            return None






