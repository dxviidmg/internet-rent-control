from email.policy import default
from enum import unique
from random import choices
from django.db import models

class Package(models.Model):
    payment_frequency_choices = (
        (1, 'Mensual'), 
        (12, 'Anual')
    )
    bandwidth = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    payment_frequency = models.IntegerField(default=1, choices=payment_frequency_choices)


    def __str__(self):
        return '{}Mbps ${}. Frecuencia: {}'.format(self.bandwidth, self.price, self.get_payment_frequency_display())

    class Meta:
        unique_together = ['bandwidth', 'price', 'payment_frequency']