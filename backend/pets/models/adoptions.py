from django.db.models.signals import post_save
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

    def safe_delete(self, user):
        if self.adopter == user:
            self.canceled_by_adopter = True
        elif self.pet.owner == user:
            self.canceled_by_owner = True
        if self.canceled_by_adopter and self.canceled_by_owner:
            return self.delete()
        else:
            return self.save()

    
def update_adoptions(sender, **kwargs):
    instance = kwargs['instance']
    created = kwargs['created']
    raw = kwargs['raw']

    if not created and not raw:
        for adoption in instance.adoptions.filter(status__name='Pending'):
            adoption.canceled_by_owner = instance.in_adoption
            adoption.save()
    
post_save.connect(update_adoptions, sender=Pet)