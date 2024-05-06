from django.db import models

# Create your models here.
class ShowRoomList(models.Model):
    name =models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
class CarList(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100,blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.name