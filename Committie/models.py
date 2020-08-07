from django.db import models


# Created models here.
class Committie(models.Model):
	Image = models.ImageField(upload_to='members/')
	Name = models.CharField(max_length=50)

	Quote = models.CharField(max_length=200)
	Linkedin = models.CharField(max_length=250)
	Category = models.CharField(max_length=10, choices=(('Faculty', 'Faculty'), ('Student', 'Student')), default='Student')
	choices = (
		('Staff Coordinator', 'Staff Coordinator'),
		('President', 'President'),
		('Vice President', 'Vice President'),
		('Secretary', 'Secretary'),
		('Joint Secretary', 'Joint Secretary'),
		('Sponsorship Head', ' Sponsorship Head'),
		('Joint Sponsorship', 'Joint Sponsorship'),
		('PR Head', 'PR Head'),
		('Joint PR', 'Joint PR'),
		('Creative Head', 'Creative Head'),
		('Joint Creative', 'Joint Creative'),
		('Technical Head', 'Technical Head'),
		('Joint Technical', 'Joint Technical'),
		('Organizing Head', 'Organizing Head'),
		('Joint Organizing', 'Joint Organizing'),
		('Magazine Head', 'Magazine Head'),
		('Joint Magazine', 'Joint Magazine'),
		('Treasurer', 'Treasurer'),
		('Membership', 'Membership')
	)
	Designation = models.CharField(max_length=50, choices=choices, default='')

	def __str__(self):
		return self.Name
