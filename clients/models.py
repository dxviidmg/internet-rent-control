from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    second_last_name = models.CharField(max_length=20)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.last_name, self.second_last_name)