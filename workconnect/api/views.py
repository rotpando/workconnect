from rest_framework.response import Response
from api.models import User, Adver
from api.serializers import UserSerializer, AdverSerializer, RegisterSerializer, LoginSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
import json
import bcrypt
''' salt must be saved in .env '''
salt = b'$2b$12$nHb8/YT3vprALE73gciI3u'

class UserList(APIView):
    def get(self,request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class AdverList(APIView):
    def get(self,request,format=None):
        isdict = isinstance(request.data, dict)
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
        if "email" in request.data:
            tickets = User.objects.filter(email=request.data['email'])
            if len(tickets) == 0:
                password = request.data['password'].encode('utf-8')
                hashed = bcrypt.hashpw(password, salt)
                user_instance = User.objects.create(email=request.data['email'],password=hashed)
                user_instance.save()
                
                print(salt)
                return Response('registered',status=status.HTTP_201_CREATED)
            else:
                return Response('error: email been taken')

        else:   
            return Response('error: bad call, no email.')

class Login(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        if "email" in request.data:
            tickets = User.objects.filter(email=request.data['email'])
            
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
        
        