from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=60, null=False)
    email = models.EmailField(null=False)
    
    def __str__(self):
        return "{} {} {}".format(self.first_name,self.last_name,self.email)