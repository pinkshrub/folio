from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kingdom(models.Model):
	name = models.CharField(max_length=70)
	notes = models.TextField()
	creator = models.ForeignKey(User, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class Card(models.Model):
	name = models.CharField(max_length=30)
	cost = models.SmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class Game(models.Model):
	creator = models.ForeignKey(User, related_name= 'creator', on_delete=models.PROTECT)
	winner = models.ForeignKey(User, related_name= 'winner', on_delete=models.PROTECT)
	kingdom = models.ForeignKey(Kingdom, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.creator + ' : ' + self.kingdom

class Kingdoms_Cards(models.Model):
	card = models.ForeignKey(Card, on_delete=models.PROTECT)
	kingdom = models.ForeignKey(Kingdom, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model):
	notes = models.CharField(max_length = 254)
	rating = models.SmallIntegerField()
	player = models.ForeignKey(User, on_delete=models.PROTECT)
	card = models.ForeignKey(Card, on_delete=models.PROTECT)
	kingdom = models.ForeignKey(Kingdom, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.player + ' rates ' + self.kingdom