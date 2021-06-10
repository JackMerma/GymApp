from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=100) 
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    trainer = models.CharField(max_length=100)

class Responsable(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    edad = models.IntegerField()
    area = models.ForeignKey(Curso, on_delete=models.CASCADE)
    delegacion = models.TextField()
    img = models.ImageField(upload_to='perfilTrainer')
    twitter = models.TextField()
    facebook = models.TextField()
    instagram = models.TextField()

