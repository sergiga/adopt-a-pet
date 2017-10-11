from django.db import models
from pets.models.adoptions import Adoption

class Message(models.Model):
    content = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User', related_name='messages')
    adoption = models.ForeignKey(Adoption, related_name='messages', on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now=True, auto_now_add=False)