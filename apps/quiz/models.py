from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=40, unique=True)
	slug = models.SlugField()
	# Takes date and time from the system in the database and it can't be updated 
	created = models.DateTimeField(auto_now_add=True)
	# On each update time can be changed
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.name