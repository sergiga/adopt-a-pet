from django.shortcuts import render
from django.http import Http404
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

class AnimalDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            raise Http404

    def get (self, request, animal_id, format=None):
        animal = self.get_object(animal_id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def put (self, request, animal_id, format=None):
        animal = self.get_object(animal_id)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, animal_id, format=None):
        animal = self.get_object(animal_id)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)