from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RESTRICTIONS = (
  ('N', 'None'),
  ('D', 'Dairy-Free'),
  ('G', 'Gluten-Free'),
  ('L', 'Lactose-Free'),
  ('N', 'Nut-Free'),
  ('S', 'Soy-Free'),
  ('V', 'Vegan')
)

STATE = [
	('AL', 'Alabama'),
	('AK', 'Alaska'),
	('AZ', 'Arizona'),
	('AR', 'Arkansas'),
	('CA', 'California'),
	('CO', 'Colorado'),
	('CT', 'Connecticut'),
	('DC', 'Washington D.C.'),
	('DE', 'Delaware'),
	('FL', 'Florida'),
	('GA', 'Georgia'),
	('HI', 'Hawaii'),
	('ID', 'Idaho'),
	('IL', 'Illinois'),
	('IN', 'Indiana'),
	('IA', 'Iowa'),
	('KS', 'Kansas'),
	('LA', 'Louisiana'),
	('ME', 'Maine'),
	('MD', 'Maryland'),
	('MA', 'Massachusetts'),
	('MI', 'Michigan'),
	('MN', 'Minnesota'),
	('MS', 'Mississippi'),
	('MO', 'Missouri'),
	('MT', 'Montana'),
	('NE', 'Nebraska'),
	('NV', 'Nevada'),
	('NH', 'New Hampshire'),
	('NJ', 'New Jersey'),
	('NM', 'New Mexico'),
	('NY', 'New York'),
	('NC', 'North Carolina'),
	('ND', 'North Dakota'),
	('OH', 'Ohio'),
	('OK', 'Oklahoma'),
	('OR', 'Oregon'),
	('PA', 'Pennsylvania'),
	('RI', 'Rhode Island'),
	('SC', 'South Carolina'),
	('SD', 'South Dakota'),
	('TN', 'Tennessee'),
	('TX', 'Texas'),
	('UT', 'Utah'),
	('VT', 'Vermont'),
	('VA', 'Virginia'),
	('WA', 'Washington'),
	('WI', 'Wisconsin'),
	('WY', 'Wyoming')
]

# Create your models here.

class Spot(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=20)
  city = models.CharField(max_length=20)
  state = models.CharField(
    max_length=2,
    choices=STATE,
    default=STATE[0][0]
  )
  zipcode = models.IntegerField('Zip')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('spots_detail', kwargs={'pk': self.id})

class Dessert(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  spots = models.ManyToManyField(Spot)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

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
