from django.db import models

# Create your models here.
class Students(models.Model): 
    gnum = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100) 

    def __str__ (self): 
        return f"G{self.gnum}: {self.name}"