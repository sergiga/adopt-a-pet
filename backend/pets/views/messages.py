from django.shortcuts import render
from django.http import Http404
from pets.models.adoptions import Adoption
from pets.models.messages import Message
from pets.serializers.messages import (
    MessageSerializer,
    MessageReadSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class MessageList(APIView):

    def get_adoption(self, id):
        try:
            return Adoption.objects.get(pk=id)
        except:
            raise Http404

    def get (self, request, id, format=None):
        adoption = self.get_adoption(id)
        messages = Message.objects.filter(adoption=adoption.id)
        serializer = MessageReadSerializer(messages, many=True)
        return Response(serializer.data)

    def post (self, request, id, format=None):
        user = request.user
        message = { 
            'content': request.data['content'], 
            'author': user.id, 
            'adoption': id, 
        }
        serializer = MessageSerializer(data=message)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)