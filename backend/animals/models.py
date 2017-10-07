from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.FloatField(blank=False)
    description = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='owners', on_delete=models.CASCADE)
    adopter = models.ForeignKey('auth.User', related_name='adopters')

    def __str__(self):
        return '%s' % (self.name)

class AnimalType(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '%s' % (self.name)