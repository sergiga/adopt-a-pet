from django.db import models
from pets.models.pets import Pet

class AdoptionStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % (self.name)

class Adoption(models.Model):
    status = models.ForeignKey(AdoptionStatus, related_name='adoptions', default=2)
    pet = models.ForeignKey(Pet, related_name='adoptions', on_delete=models.CASCADE)
    adopter = models.ForeignKey('auth.User', related_name='adoptions', null=True)
    canceled_by_owner = models.BooleanField(blank=False, default=False)
    canceled_by_adopter = models.BooleanField(blank=False, default=False)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)