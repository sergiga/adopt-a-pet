from rest_framework import serializers
from pets.models.pets import Pet, PetType
from pets.serializers.users import UserSerializer

class PetSerializer(serializers.ModelSerializer):
    pet_type = serializers.SlugRelatedField(
        slug_field='name', 
        queryset = PetType.objects.all()
    )

    class Meta:
        model = Pet
        fields = ('id', 'name', 'age', 'description', 
                  'in_adoption', 'owner', 'pet_type')

class PetReadSerializer(PetSerializer):
    owner = UserSerializer(read_only=True)