from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=35, null=False)
    description = models.TextField(max_length=256, null=False)
    pub_date = models.DateField(null=False)
    
    def __str__(self):
        return "{} {} {}".format(self.title,self.description,self.pub_date)