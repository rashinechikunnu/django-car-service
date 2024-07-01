from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


# LOGIN

class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default = False)
   
    
# customer models

class Customer_data(models.Model):
    user = models.ForeignKey(Login,on_delete= models.CASCADE)
    Name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email=models.EmailField()
    license_no = models.CharField(max_length=8)


    def __str__(self):
        return self.Name
    
# manager models

class manager_data(models.Model):
    user = models.ForeignKey(Login,on_delete= models.CASCADE)
    Name=models.CharField(max_length=100)
    employee_no=models.CharField(max_length=4)
    contact=models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.Name
    


class Feedback(models.Model):
    user = models.ForeignKey(Customer_data,on_delete=models.DO_NOTHING)
    text_me = models.TextField()
    date = models.DateField(auto_now_add=True)
    replay = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.text_me
    
class shedules(models.Model):
    date = models.DateField()
    starting_time = models.TimeField()
    ending_time = models.TimeField()

    
    

class customer_booking(models.Model):
    user= models.ForeignKey(Customer_data,on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(shedules,on_delete=models.DO_NOTHING)
    car_name = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=15)
    status = models.IntegerField(default=0)
    


    
    

    