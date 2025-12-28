from django.db import models

# Create your models here.

class Ceo(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.CharField(max_length=100)



class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()