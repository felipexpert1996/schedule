from rest_framework.serializers import ModelSerializer
from .models import Event
from authentication.models import CustomUser
from authentication.serializer import UserSerializer


class EventSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True, help_text='usuário do evento')
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        del validated_data['user']
        user = CustomUser.objects.get(uuid=user)
        event = Event.objects.create(**validated_data)
        event.user = user
        event.save()
        return event
