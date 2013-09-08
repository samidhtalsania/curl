from django.db import models

# Create your models here.

class urls(models.Model):
	url = models.CharField(max_length=250)

	def __unicode__(self):
		return self.url



		
