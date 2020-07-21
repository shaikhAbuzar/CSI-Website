from django.db import models

# Create your models here.
class Committie(models.Model):
    image = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name