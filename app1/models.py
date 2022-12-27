from django.db import models

# Create your models here.

class Employee(models.Model):

	Eno = models.IntegerField()

	Ename = models.CharField(max_length=20)

	Esal = models.IntegerField()

	Eadd = models.CharField(max_length=50)
