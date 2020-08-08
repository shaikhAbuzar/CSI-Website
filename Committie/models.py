from django.db import models


# Created models here.
class Committie(models.Model):
	Image = models.ImageField(upload_to='members/')
	Name = models.CharField(max_length=50)
	Linkedin = models.URLField(blank=True)
	Category = models.CharField(max_length=10, choices=(('Faculty', 'Faculty'), ('Student', 'Student')), default='Student')
	choices = (
		('Incharge', 'Incharge'),
		('Staff Coordinator', 'Staff Coordinator'),
		('President', 'President'),
		('Vice President', 'Vice President'),
		('Secretary', 'Secretary'),
		('Joint Secretary', 'Joint Secretary'),
		('Sponsorship Head', ' Sponsorship Head'),
		('Joint Sponsorship Head', 'Joint Sponsorship Head'),
		('PR Head', 'PR Head'),
		('Joint PR Head', 'Joint PR Head'),
		('Creative Head', 'Creative Head'),
		('Joint Creative Head', 'Joint Creative Head'),
		('Technical Head', 'Technical Head'),
		('Joint Technical Head', 'Joint Technical Head'),
		('Organizing Head', 'Organizing Head'),
		('Joint Organizing Head', 'Joint Organizing Head'),
		('Magazine Head', 'Magazine Head'),
		('Joint Magazine Head', 'Joint Magazine Head'),
		('Treasurer', 'Treasurer'),
		('Joint Treasurer', 'Joint Treasurer')
	)
	Designation = models.CharField(max_length=50, choices=choices, default='')

	def __str__(self):
		return self.Designation + '-' + self.Name
