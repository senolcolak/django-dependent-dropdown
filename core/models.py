from unicodedata import name
from django.db import models

# Create your models here.



class Country(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return '%s' % (self.name)


class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='citys')
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.name,self.country)

class District(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name='districts')
    name = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return '%s %s %s' % (self.name,self.city,self.city.country)

class Event(models.Model):
    location = models.ForeignKey(District,on_delete=models.CASCADE,related_name='events')
    name = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return '%s' % (self.name)