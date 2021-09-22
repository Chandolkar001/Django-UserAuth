from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	phone = models.IntegerField()
	gender = models.CharField(max_length = 1, choices=(('m','Male'), ('f', 'Female'), ('o', 'Other')), blank=True, null=True)

	def __str__(self):
		return f'{self.user.username}'