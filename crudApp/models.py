from django.db import models
from django.utils.translation import gettext as _

# ImageField requires the Pillow library to be installed
# think of images as MEDIA file; we are going to upload/save them to our "media/" dir itself
# we won't upload them to database
# we recieve these images files somewhere else and in databse, we store location of image(url)
# so we are saving text and not image in the database
import sys
sys.path.append("D:\Projects\Django\CRUD with Django\crud\packages")


# Create your models here.
class Employee(models.Model):
    # 'id' can only be used as a field name if the field also sets 'primary_key=True
    id = models.CharField(max_length=7,primary_key=True)
    checkbox = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=200)
    phone = models.IntegerField()
    profileImg = models.ImageField(upload_to='images/',blank=True, null=False)

    def __str__(self):
        return self.name

    

