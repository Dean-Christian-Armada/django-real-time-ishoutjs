from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from drealtime import iShoutClient
ishout_client = iShoutClient()

# Create your models here.
class Section(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		users = User.objects.filter()
		for x in users:
			ishout_client.emit(
				x.id,
				'alertchannel',
				data={'msg':'%s has been added' % self.name}
			)
		super(Section, self).save(*args, **kwargs)