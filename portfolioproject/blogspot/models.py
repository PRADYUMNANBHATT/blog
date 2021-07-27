from portfolioproject.settings import TIME_ZONE
from django.db import models

class all_blog(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField()
 date_published = models.DateField()
 image = models.ImageField(blank=True,upload_to='portfolio/images/')
 #image=models.ImageField(blank=True,upload_to='portfolio/images')

 def __str__(self):
     return self.title

# Create your models here.
