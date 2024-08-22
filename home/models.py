from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserScore(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    usern=models.CharField(max_length=120, null=True)
    gk=models.CharField(max_length=120, null=True)
    computer=models.CharField(max_length=120, null=True)
    science=models.CharField(max_length=120, null=True)
    sports=models.CharField(max_length=120, null=True)
    animals=models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.usern
    
class Gk(models.Model):
    id=models.BigAutoField(primary_key=True)
    question=models.CharField(max_length=400, null=False)
    correct=models.CharField(max_length=400, null=False)
    incorrect1=models.CharField(max_length=400, null=False)
    incorrect2=models.CharField(max_length=400, null=False)
    incorrect3=models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.question
    
class Computer(models.Model):
    id=models.BigAutoField(primary_key=True)
    question=models.CharField(max_length=400, null=False)
    correct=models.CharField(max_length=400, null=False)
    incorrect1=models.CharField(max_length=400, null=False)
    incorrect2=models.CharField(max_length=400, null=False)
    incorrect3=models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.question
    
class Animal(models.Model):
    id=models.BigAutoField(primary_key=True)
    question=models.CharField(max_length=400, null=False)
    correct=models.CharField(max_length=400, null=False)
    incorrect1=models.CharField(max_length=400, null=False)
    incorrect2=models.CharField(max_length=400, null=False)
    incorrect3=models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.question
    
class Sport(models.Model):
    id=models.BigAutoField(primary_key=True)
    question=models.CharField(max_length=400, null=False)
    correct=models.CharField(max_length=400, null=False)
    incorrect1=models.CharField(max_length=400, null=False)
    incorrect2=models.CharField(max_length=400, null=False)
    incorrect3=models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.question
    
class Science(models.Model):
    id=models.BigAutoField(primary_key=True)
    question=models.CharField(max_length=400, null=False)
    correct=models.CharField(max_length=400, null=False)
    incorrect1=models.CharField(max_length=400, null=False)
    incorrect2=models.CharField(max_length=400, null=False)
    incorrect3=models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.question

    