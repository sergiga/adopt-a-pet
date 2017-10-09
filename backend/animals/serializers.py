from rest_framework import serializers
from animals.models import Animal, AnimalType

class AnimalSerializer(serializers.ModelSerializer):
    animal_type = serializers.SlugRelatedField(
        slug_field='name', 
        queryset = AnimalType.objects.all()
    )

    class Meta:
        model = Animal
        fields = ('id', 'name', 'age', 'description', 
                  'owner', 'adopter', 'animal_type')