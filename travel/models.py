from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Traveler(models.Model):
	def __str__(self):
		return self.user.username

	traveler_yet = models.BooleanField(default=False)  # the user is not a coder yet
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created = models.DateField(auto_now=True)   # maybe redundant, user model has date_joined
	updated = models.DateField(auto_now=True)
