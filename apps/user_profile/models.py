from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	# Bottom one is bad practice
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	# Now put all these as null
	mobile = models.CharField(max_length=15, null=True, blank=True)
	address = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.user.username, self.mobile)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
