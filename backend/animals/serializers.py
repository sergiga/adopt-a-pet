from rest_framework import serializers
from animals.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = Animal
        fields = ('id', 'name', 'age', 'description'.
                  'owner', 'adopter', 'type')