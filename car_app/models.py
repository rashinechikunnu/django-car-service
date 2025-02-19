from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


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
    

#admin/customer
class Feedback(models.Model):
    user = models.ForeignKey(Customer_data,on_delete=models.DO_NOTHING)
    text_me = models.TextField()
    date = models.DateField(auto_now_add=True)
    replay = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.text_me
 
#customer /admin 
class shedules(models.Model):
    date = models.DateField()
    starting_time = models.TimeField()
    ending_time = models.TimeField()

    def __str__(self):
        return self.starting_time
    

    

#customer/manager
class customer_booking(models.Model):
    user= models.ForeignKey(Customer_data,on_delete=models.CASCADE)
    schedule = models.ForeignKey(shedules,on_delete=models.CASCADE)
    car_name = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=15)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name
    

#admin/manager
class create_work(models.Model):
    Name_manager = models.ForeignKey(manager_data,on_delete=models.CASCADE)
    customer_booking_id= models.ForeignKey(customer_booking,on_delete=models.CASCADE,null=True,blank=True)
    vehicle_type =(
                    ("sedan","sedan"),
                    ("SUV","SUV"),
                    ("hatchback","hatchback"),
                    ("others","others")
    )
    vehicle = models.CharField(max_length=50,choices=vehicle_type,null=True,blank=True)

    complaint_description = models.TextField(null=True,blank=True)
    choice =(
            ("Work started","Work started"),
            ("Work on progres","work on progres"),
            ("work compleated","work compleated"),
    )
    work_status = models.CharField(max_length=50,choices=choice,null=True,blank=True)
    estimate_cost = models.CharField(max_length=20,null=True,blank=True)
    payment_status=models.IntegerField(default=0)



# payment

class payment(models.Model):
    work=models.ForeignKey(create_work,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    cvv=models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=7)
    

    
    

    