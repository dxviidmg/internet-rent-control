from django.db import models

class Package(models.Model):
    bandwidth = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()


    def __str__(self):
        return '{}Mbps ${}'.format(self.bandwidth, self.price)