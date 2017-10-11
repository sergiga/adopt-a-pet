from rest_framework import serializers
from pets.models.messages import Message
from pets.serializers.users import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'author', 'adoption', 'received_at')

class MessageReadSerializer(MessageSerializer):
    author = UserSerializer(read_only=True)