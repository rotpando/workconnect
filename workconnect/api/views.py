from rest_framework.response import Response
from api.models import UserProfile, Adver
from api.serializers import UserSerializer, AdverSerializer, RegisterSerializer, LoginSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from rest_framework import status
import json


class UserList(APIView):
    def get(self,request,format=None):
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class AdverList(APIView):
    def get(self,request,format=None):
        isdict=type(request.data)
        
        if isdict:
            
            try:
                if request.data['pageNumber']:
                    try:
                        pageNumber=int(request.data['pageNumber'])
                        if pageNumber > 0:
                            advers = Adver.objects.all()
                            if len(advers) > 0:
                                serializer = AdverSerializer(advers, many=True)
                                return Response(serializer.data[(pageNumber*10)-10:(pageNumber*10)],status=status.HTTP_202_ACCEPTED)
                            else:
                                return Response("[]")
                        else:
                            raise ValueError('pageNumber must be upper than 0')
                    except:
                        return Response("Invalid pageNumber")
            except:
                return Response("Invalid request")
        else:
            return Response("Invalid request")



class RegisterUser(APIView):
    def post(self,request,format=None):
        serializer = RegisterSerializer(request.data)
        print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response("registered",status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
        
class Login(APIView):
    
    def post(self,request,format=None):

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        if "email" in request.data:
            tickets = UserProfile.objects.filter(email=request.data['email'])
            
            if len(tickets) == 0:
                return Response('No user found')
            else:
                password = request.data['password'].encode('utf-8')
                hashed = bcrypt.hashpw(password, salt)
                hashedDecoded = hashed.decode('utf-8')
                prueba = tickets[0].password[2:-1]
                print (len(hashedDecoded),prueba)
                if hashedDecoded == prueba:
                    print("paso!")
                serializer = LoginSerializer("kk", many=True)
                return Response('logued!',status=status.HTTP_202_ACCEPTED)
            

        else:
            return Response('error: wrong login data',status=status.HTTP_202_ACCEPTED)
        
        