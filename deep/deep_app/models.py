from distutils.command.upload import upload
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
  image = models.ImageField(upload_to="uploads/images",blank=True)      #for this -> pip install pillow
  name = models.CharField(max_length=100,blank=False)
  price = models.DecimalField(max_digits=7,decimal_places=2,blank=False)
  desciption = models.TextField(blank=True)
  category = models.CharField(max_length=50,blank=True)

  def __int__(self):
    return self.id