from django.db import models

# Create your models here.
class Caste(models.Model):
    caste_name = models.CharField(max_length=20)
    def __str__(self)->str:
        return self.caste_name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.TextField()
    caste = models.ForeignKey(Caste, null=True, blank=True, on_delete=models.CASCADE, related_name='castes')

