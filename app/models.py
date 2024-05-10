from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User



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
    showroom = models.ForeignKey(ShowRoomList, on_delete=models.CASCADE, null=True, related_name="Showrooms")

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating =models.IntegerField(validators=[MinValueValidator,MaxValueValidator])
    comments = models.CharField(max_length=200, null=True)
    car = models.ForeignKey(CarList, on_delete=models.CASCADE, related_name="Reviews", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The Rating of {self.car.name}:--- {self.rating}"