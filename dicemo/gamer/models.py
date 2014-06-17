from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField

class Gamer(models.Model):
	user            = models.OneToOneField(User)
	name            = models.CharField(max_length=100)
	description		= models.TextField(blank=True)
	joined_date		= models.DateTimeField(auto_now_add=True)
	img				= FilerImageField(null=True, blank=True, help_text='Upload bio pic') 

	def __unicode__(self):
		return self.name
