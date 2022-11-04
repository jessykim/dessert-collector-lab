from django.db import models

# Create your models here.
class Dessert(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name