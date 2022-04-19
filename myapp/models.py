

from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):  
    username    = models.CharField(max_length=20)  
    email   = models.CharField(max_length=100)  
    password = models.CharField(max_length=15)  
 
  
    class Meta:  
        db_table = "employee" 
