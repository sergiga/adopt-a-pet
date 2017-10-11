from django.db import models
from pets.models.pets import Pet

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, related_name='adoptions', on_delete=models.CASCADE)
    adopter = models.ForeignKey('auth.User', related_name='adoptions', null=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)