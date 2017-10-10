from django.shortcuts import render
from django.http import Http404
from pets.models import Pet
from pets.models import Adoption
from pets.serializers import (
    PetSerializer,
    PetReadSerializer,
    AdoptionSerializer, 
    AdoptionReadSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class PetList(APIView):

    def get(self, request, format=None):
        user = request.user
        pets = Pet.objects.filter(owner=user)
        serializer = PetReadSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404

    def get (self, request, pet_id, format=None):
        pet = self.get_object(pet_id)
        serializer = PetReadSerializer(pet)
        return Response(serializer.data)

    def put (self, request, pet_id, format=None):
        pet = self.get_object(pet_id)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pet_id, format=None):
        pet = self.get_object(pet_id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdoptionDetail(APIView):

    def get_object(self, pet_id, adopter_id):
        try:
            return Adoption.objects.get(
                pet=pet_id, 
                adopter=adopter_id
            )
        except Adoption.DoesNotExist:
            raise Http404

    def get (self, request, pet_id, adopter_id, format=None):
        adoption = self.get_object(pet_id, adopter_id)
        serializer = AdoptionReadSerializer(adoption)
        return Response(serializer.data)

    def post (self, request, pet_id, adopter_id, format=None):
        adoption = { 'pet': pet_id, 'adopter': adopter_id }
        serializer = AdoptionSerializer(data=adoption)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
