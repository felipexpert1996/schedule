from asyncore import write
from rest_framework.serializers import ModelSerializer, CharField
from .models import Event
from authentication.models import CustomUser
from rest_framework.exceptions import ValidationError

class EventSerializer(ModelSerializer):

    uuid = CharField(write_only=True)

    class Meta:
        model = Event
        fields = ['uuid', 'start_date', 'start_time', 'end_date', 'end_time', 'all_day']

    def create(self, validated_data):
        try:
            event = Event.objects.create(
                user = CustomUser.objects.get(uuid=validated_data['uuid']),
                start_date = validated_data['start_date'],
                start_time = validated_data['start_time'],
                end_date = validated_data['end_date'],
                end_time = validated_data['end_time'],
                all_day = validated_data['all_day']
            )
            return event
        except:
            return ValidationError(detail={'user': 'User not found'}, code=500)
        
