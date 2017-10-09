from django.shortcuts import render
from animals.models import Animal
from animals.serializers import AnimalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class AnimalList(APIView):

    def get(self, request, format=None):
        user = request.user
        animals = Animal.objects.filter(owner=user)
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)