from django.db import models
from django.utils.text import slugify

# from django.utils.translation import gettext_lazy as _
# See this translation module


class Category(models.Model):
	name = models.CharField(max_length=40, unique=True)
	slug = models.SlugField(blank=True, unique=True)
	# Takes date and time from the system in the database and it can't be updated 
	created = models.DateTimeField(auto_now_add=True)
	# On each update time can be changed
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		# return _(self.name)
		return self.name