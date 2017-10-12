from django.shortcuts import render
from django.http import Http404
from pets.models.pets import Pet
from pets.serializers.pets import (
    PetSerializer,
    PetReadSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from pets.permissions.permissions import IsOwnerOrReadOnly
import json

class PetList(APIView):

    def get(self, request, format=None):
        user = request.user
        pets = Pet.objects.filter(owner=user)
        if request.GET.__contains__('in_adoption'):
            in_adoption = json.loads(request.GET.get('in_adoption'))
            pets = pets.filter(in_adoption=in_adoption)
        serializer = PetReadSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetail(APIView):
    
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )

    def get_object(self, pk):
        try:
            obj = Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

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