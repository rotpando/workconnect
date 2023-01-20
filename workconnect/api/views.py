from rest_framework.response import Response
from api.models import User, Adver
from api.serializers import UserSerializer, AdverSerializer
from django.shortcuts import render
from rest_framework.views import APIView
import json

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
                                return Response(serializer.data[(pageNumber*10)-10:(pageNumber*10)])
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