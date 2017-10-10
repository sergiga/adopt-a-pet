from django.db import models

class PetType(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return '%s' % (self.name)

class Pet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.FloatField(blank=False)
    description = models.TextField(blank=False)
    in_adoption = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey('auth.User', related_name='pets', on_delete=models.CASCADE)
    pet_type = models.ForeignKey(PetType, related_name='pets', null=True)

    def __str__(self):
        return '%s' % (self.name)

class Adoption(models.Model):
    animal = models.ForeignKey(Pet, related_name='adoptions')
    adopter = models.ForeignKey('auth.User', related_name='adoptions', null=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)