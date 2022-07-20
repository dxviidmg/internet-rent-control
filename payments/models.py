from django.db import models
from services.models import Service, TimeStampedModel


class Payment(TimeStampedModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='payments')
    end_of_validity = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '#{}'.format(self.pk)