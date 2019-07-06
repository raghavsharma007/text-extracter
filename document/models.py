from django.db import models

class Form(models.Model):
    select = models.CharField(choices=(('Driving Licence','Driving Licence'),('Passport', 'Passport'),('other', 'other')),
                              max_length=10,default= 'Passport', null = True)
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='document/media/',blank = True)


    def __str__(self):
        return self.name
