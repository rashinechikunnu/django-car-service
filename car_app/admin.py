from django.contrib import admin
from . models import Customer_data,manager_data,Login,Feedback

# Register your models here.

# customer_data register
admin.site.register(Customer_data),

# manager_data register
admin.site.register(manager_data),

# login_data register
admin.site.register(Login),

# feedback
admin.site.register(Feedback)
