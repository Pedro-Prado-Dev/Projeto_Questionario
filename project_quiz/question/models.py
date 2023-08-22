from django.db import models

# Create your models here.
class Quest (models.Model):
    question = models.CharField(max_length=10000)
    alt_a= models.CharField( max_length=100)
    alt_b= models.CharField( max_length=100)
    alt_c= models.CharField( max_length=100)
    alt_d= models.CharField( max_length=100)
    resp = models.CharField( max_length=100)
    
    def __str__(self):
        return self.resp
    