from distutils.command.upload import upload
from django.db import models

# Create your models here.

class logo(models.Model):
    logo_img = models.ImageField(upload_to = "logo")
class quotes(models.Model):
    quote_text = models.CharField(max_length=500)

class Logoimage(models.Model):
    image = models.ImageField(upload_to = 'pics')

class Dailyquotes(models.Model):
     logo = models.CharField(max_length=400)
   
    
