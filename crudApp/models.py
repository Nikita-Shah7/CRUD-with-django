from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Employee(models.Model):
    # 'id' can only be used as a field name if the field also sets 'primary_key=True
    id = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    

