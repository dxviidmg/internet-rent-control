from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    second_last_name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.second_last_name)
        
        
class Client(Person):
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    belongs_to_partner = models.BooleanField(default=False) 

