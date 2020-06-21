from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
	owner = models.ForeignKey(User, to_field="username",on_delete=models.CASCADE)
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)


	def __str__(self):
		return self.item + ' | ' + str(self.completed) + str(self.owner)
		 