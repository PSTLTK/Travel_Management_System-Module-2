from django.db import models
from datetime import datetime
from django.utils.timezone import timezone
from django.contrib.auth.models import User

# Create your models here.

class ContinentModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DestinationModel(models.Model):
    id               = models.AutoField(primary_key=True)
    place            = models.CharField(max_length=100)
    country          = models.CharField(max_length=100)
    continent        = models.ForeignKey(ContinentModel,on_delete=models.CASCADE,default=None)
    flight_price     = models.IntegerField(default=None)
    adult_per_day    = models.IntegerField(default=15000)
    child_per_day    = models.IntegerField(default=10000)
    main_image       = models.ImageField(default=None)
    image_a          = models.ImageField(default=None)
    image_b          = models.ImageField(default=None)
    image_c          = models.ImageField(default=None)
    description      = models.TextField(default=None)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.place
    
class RegisterationModel(models.Model):
    address = models.TextField(default=None)
    phone = models.CharField(max_length=100)
    profile = models.ImageField(default=None)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.address

class BookingModel(models.Model):
    b_code= models.CharField(max_length=20, null=True)
    b_name= models.CharField(max_length=225,null = True)
    b_email= models.EmailField(default=None,null=True)
    b_phone= models.CharField(max_length=20,null=True)
    b_date= models.DateField(default=None)
    duration= models.CharField(max_length=150, null=True)
    b_trip= models.CharField(max_length=100,null=True)
    total_cost= models.BigIntegerField(default=None)
    b_status= models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    travel = models.ForeignKey(DestinationModel,on_delete=models.CASCADE,default=None)
    booked_at = models.DateTimeField(default=datetime.now)
    
class FeedbackModel(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.message
     