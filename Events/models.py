from django.db import models


# Created models here.
class Event(models.Model):
	poster = models.ImageField(upload_to='EventPosters')
	title = models.CharField(max_length=200)
	event_date = models.DateField()
	event_time = models.TimeField()
	description = models.TextField(max_length=350)
	STATUS = (('upcoming', 'upcoming'), ('completed', 'completed'))
	status = models.CharField(max_length=10, choices=STATUS, default='upcoming')
	registration_url = models.URLField()
	report = models.TextField(blank=True)
	images_url = models.URLField(blank=True)
	# TODO Add visual graphs
	event_image1 = models.ImageField(upload_to='EventImages', blank=True)
	event_image2 = models.ImageField(upload_to='EventImages', blank=True)
	event_image3 = models.ImageField(upload_to='EventImages', blank=True)

	def __str__(self):
		return self.title
