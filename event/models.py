from operator import mod
from statistics import mode
from django.db import models
from authentication.models import CustomUser


class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField(help_text='Data inicial do evento')
    start_time = models.TimeField(help_text='Hora inicial do evento')
    end_date = models.DateField(help_text='Data final do evento')
    end_time = models.TimeField(help_text='Hora final do evento')
    all_day = models.BooleanField(help_text='O evento vai durar o dia inteiro?')

    def __str__(self):
        return f'{self.user} {self.start_date} - {self.end_date}'
