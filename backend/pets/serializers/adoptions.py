from rest_framework import serializers
from pets.models.adoptions import Adoption
from pets.serializers.pets import PetReadSerializer
from pets.serializers.users import UserSerializer
from django.contrib.auth.models import User

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ('id', 'pet', 'adopter', 'updated_at')

class AdoptionReadSerializer(AdoptionSerializer):
    pet = PetReadSerializer(read_only=True)
    adopter = UserSerializer(read_only=True)