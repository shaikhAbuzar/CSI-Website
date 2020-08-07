from django.db import models


# Created models here.
class Blogs(models.Model):
	cover_pic = models.ImageField(upload_to='BlogCovers')
	title = models.CharField(max_length=500)
	writer_pic = models.ImageField(upload_to='UserPhotos', blank=True)
	writer_name = models.CharField(max_length=300)
	insta_id = models.URLField(blank=True)
	twitter_id = models.URLField(blank=True)
	linkedin_id = models.URLField(blank=True)
	date_of_article = models.DateField()
	article = models.TextField()

	def __str__(self):
		return self.title
