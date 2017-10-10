from rest_framework import serializers
from pets.models import Pet, PetType

class PetSerializer(serializers.ModelSerializer):
    pet_type = serializers.SlugRelatedField(
        slug_field='name', 
        queryset = PetType.objects.all()
    )

    class Meta:
        model = Pet
        fields = ('id', 'name', 'age', 'description', 
                  'in_adoption', 'owner', 'pet_type')