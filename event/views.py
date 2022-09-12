from rest_framework.viewsets import ModelViewSet
from .models import Event
from .serializer import EventSerializer
from django.views.generic import TemplateView


class EventViewset(ModelViewSet):
    """
    list:
    Retorna uma lista de eventos cadastrados

    create:
    Cria um evento para o usuário especifico

    delete:
    Deleta um evento especifico

    read:
    Mostra detalhes de um evento

    update:
    Atualiza dados de um evento

    partial_update:
    Atualiza algum dado de um evento
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventTemplateViewset(TemplateView):
    template_name = 'event/callendar.html'
