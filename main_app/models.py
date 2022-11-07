from django.db import models
from django.urls import reverse

RESTRICTIONS = (
  ('N', 'None'),
  ('D', 'Dairy-Free'),
  ('G', 'Gluten-Free'),
  ('L', 'Lactose-Free'),
  ('N', 'Nut-Free'),
  ('S', 'Soy-Free'),
  ('V', 'Vegan')
)

# Create your models here.
class Dessert(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('desserts_detail', kwargs={'dessert_id': self.id})

class Recipe(models.Model):
  name = models.CharField(max_length=50)
  restrictions = models.CharField(
    'Dietary Restrictions',
    max_length=1,
    choices=RESTRICTIONS,
    default=RESTRICTIONS[0][0]
  )
  url = models.URLField(
    'Link to Recipe',
    max_length=200
  )

  dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_restrictions_display()}"