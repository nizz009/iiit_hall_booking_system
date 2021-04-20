from django.db import models
from accounts.models import User
from django.urls import reverse
from .choices import *

class Hall_1(models.Model):
	name = models.CharField(max_length = 150)
	purpose = models.TextField()
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __str__(self):
		return self.name


class Hall_2(models.Model):
	name = models.CharField(max_length = 150)
	purpose = models.TextField()
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __str__(self):
		return self.name


class Hall_3(models.Model):
	name = models.CharField(max_length = 150)
	purpose = models.TextField()
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __str__(self):
		return self.name


class Application(models.Model):
	hall_name = models.CharField(max_length = 150, choices = HALL_NAMES, default = "Mini Audi")  
	name = models.CharField(max_length = 150)
	purpose = models.TextField()
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	approve = models.CharField(max_length = 2, default = "p")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('application-detail', kwargs={'pk': self.pk})