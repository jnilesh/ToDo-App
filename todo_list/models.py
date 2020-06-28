from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
	author = models.CharField(max_length=50)
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)


	def __str__(self):
		return self.item + ' | ' + str(self.completed) 
