from django.db import models


# Created models here.
class CarouselSlider(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=75)
	short_description = models.TextField()

	def __str__(self):
		return self.title
