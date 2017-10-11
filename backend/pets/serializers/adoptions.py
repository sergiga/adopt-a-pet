from django.db.models.signals import post_save
from rest_framework import serializers
from pets.models.adoptions import Adoption, AdoptionStatus
from pets.serializers.pets import PetReadSerializer
from pets.serializers.users import UserSerializer
from pets.models.pets import Pet

class AdoptionSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset = AdoptionStatus.objects.all(),
    )
    class Meta:
        model = Adoption
        fields = ('id', 'status', 'pet', 'adopter',
                  'canceled_by_owner', 'canceled_by_adopter', 'updated_at')

class AdoptionReadSerializer(AdoptionSerializer):
    pet = PetReadSerializer(read_only=True)
    adopter = UserSerializer(read_only=True)

def update_adoptions(sender, **kwargs):
    instance = kwargs['instance']
    created = kwargs['created']
    raw = kwargs['raw']

    if not created and not raw:
        for adoption in instance.adoptions.filter(status__name='Pending'):
            adoption.canceled_by_owner = instance.in_adoption
            adoption.save()
    
post_save.connect(update_adoptions, sender=Pet)