from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Nombre')
    last_name = models.CharField(max_length=20, verbose_name='Apellido paterno')
    second_last_name = models.CharField(max_length=20,verbose_name='Apellido materno')

    class Meta:
        abstract = True
    
    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.second_last_name).strip()

    def __str__(self):
        return self.get_full_name()
        
        
class Client(Person):
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    belongs_to_partner = models.BooleanField(default=False) 

