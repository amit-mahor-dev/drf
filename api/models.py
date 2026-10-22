from django.db import models

# Create your models here.

class student(models.Model):
    name  = models.CharField(max_length = 50, db_index=True)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=60)
    
    class Meta:
        db_table = "student"
    # def __str__(self):
    #     return self.name+self.city+"puriya"
    
class book(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    class Meta:
        db_table = "book"
    
