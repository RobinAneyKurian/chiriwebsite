from django.db import models

# Create your models here.

class logo(models.Model):
    logo_img = models.ImageField(upload_to = "logo")
   
    
