from rest_framework import serializers
from pets.models.adoptions import Adoption, AdoptionStatus
from pets.serializers.pets import PetReadSerializer
from pets.serializers.users import UserSerializer

class AdoptionSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset = AdoptionStatus.objects.all(),
    )
    class Meta:
        model = Adoption
        fields = ('id', 'status', 'pet', 'adopter', 'updated_at')

class AdoptionReadSerializer(AdoptionSerializer):
    pet = PetReadSerializer(read_only=True)
    adopter = UserSerializer(read_only=True)