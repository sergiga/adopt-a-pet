from django.shortcuts import render
from django.http import Http404
from pets.models.adoptions import Adoption
from pets.serializers.adoptions import (
    AdoptionSerializer, 
    AdoptionReadSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from pets.permissions.adoptions import IsOwnerOrAdopter

class AdoptionList(APIView):

    def get (self, request, format=None, **kwargs):
        adoptions = Adoption.objects.filter(**kwargs)
        serializer = AdoptionReadSerializer(adoptions, many=True)
        return Response(serializer.data)

class AdoptionDetail(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrAdopter,
    )

    def get_object(self, pet_id, adopter_id):
        try:
            obj = Adoption.objects.get(
                pet=pet_id, 
                adopter=adopter_id
            )
        except Adoption.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

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

    def put (self, request, pet_id, adopter_id, format=None):
        adoption = self.get_object(pet_id, adopter_id)
        serializer = AdoptionSerializer(adoption, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pet_id, adopter_id, format=None):
        adoption = self.get_object(pet_id, adopter_id)
        adoption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
