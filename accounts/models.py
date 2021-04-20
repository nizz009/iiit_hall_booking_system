from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class User(AbstractUser):
	is_admin = models.CharField(max_length=6, default="False")
	email = models.EmailField()


class Student(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
	name = models.CharField(max_length = 10)

	def __str__(self):
		return self.user.username

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
	designation = models.CharField(max_length = 50)

	def __str__(self):
		return self.user.username

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

		if img.height != img.width:
			output_size = (100, 100)
			img.thumbnail(output_size)
			img.save(self.image.path)