from django.shortcuts import render,redirect
from .forms import ManagerForms,LoginForms
from .models import customer_booking


def manager_page(request):

   


    
    return render(request,'manager_page/manager.html')


def customer_booking_list(request):
    customer_book_view = customer_booking.objects.all()
    
    return render(request,'manager_page/customer_booking.html',{'customer_book_view':customer_book_view})


