from django.db import models
from django.conf import settings

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)


	def __str__(self):
		return self.item + ' | ' + str(self.completed) + str(self.owner)
		 