
from django.shortcuts import render,redirect
from .forms import CustomerForms,LoginForms
from .forms import LoginForms,feedbackForms,Customer_booking_Forms,paymentForms
from .models import Customer_data,Feedback,shedules,customer_booking,create_work
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# customer page
def customer_page(request):
    return render(request,"customer_page/customer.html")


# customer account creation
def customer_account_creation(request):
    form1 = LoginForms()
    form2 = CustomerForms()
    if request.method == "POST":
        form1 = LoginForms(request.POST)
        form2 = CustomerForms(request.POST)
        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1= form2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect('logIN')
    return render(request,"main_page.html",{'form1':form1,'form2':form2})

# add feedback
@login_required(login_url='logIN')
def feedback_customer(request):
    adduser = request.user
    data = Customer_data.objects.get(user = adduser)
    if request.method == 'POST':
        feed_back= feedbackForms(request.POST)
        if feed_back.is_valid():
            obj = feed_back.save(commit = False)
            obj.user = data
            obj.save()
            return redirect('feedback_views')
    else:
        feed_back=feedbackForms()
    return render(request,"customer_page/feedback.html",{'feed_back':feed_back})

# feedback view
@login_required(login_url='logIN')
def feedback_view(request):
    feedback_user = request.user
    fdb = Customer_data.objects.get(user=feedback_user)
    feed_view = Feedback.objects.filter(user=fdb)
    return render(request,'customer_page/feedback_views.html',{'feed_view':feed_view})

# work time
@login_required(login_url='logIN')
def schedule_time(request):
    schedule_time=shedules.objects.all()
    return render(request,'customer_page/schedule_time.html',{'schedule_time':schedule_time})

# booking
@login_required(login_url='logIN')
def booking_customer(request,pk):
    adduser1 = request.user
    data1 = Customer_data.objects.get(user = adduser1) 
    data2 = shedules.objects.get(pk=pk)
    booking = customer_booking.objects.filter(user = data1, schedule = data2)
    if booking.exists():
        messages.info( request," have already booked this schedule")
        return redirect('view_schedule')
    elif request.method == 'POST':
            customer_books= Customer_booking_Forms(request.POST)
            if customer_books.is_valid():
                object1 = customer_books.save(commit = False)
                object1.user = data1
                object1.schedule= data2
                object1.save()
                messages.info(request,"Booking succesfull")
                return redirect('booking_list')
    else:
          customer_books=Customer_booking_Forms()
    return render(request,"customer_page/c_booking.html",{"cust_booking":customer_books})

# view booking status
@login_required(login_url='logIN')
def booking_views(request):
    data = request.user
    data = Customer_data.objects.get(user=data)
    booking_status = customer_booking.objects.filter(user=data)
    return render(request,"customer_page/booking_list.html",{'booking_status':booking_status})

# view work status
@login_required(login_url='logIN')
def work_status(request):
    customer_user = request.user
    work_users = Customer_data.objects.get( user= customer_user)
    status_work = create_work.objects.filter(customer_booking_id__user=work_users)
    return render(request,'customer_page/work_status.html',{'status_work':status_work})

# payment
@login_required(login_url='logIN')
def payment(request,pk):
    c_work = create_work.objects.get(pk=pk)
    if request.method == 'POST':
        payform = paymentForms(request.POST)
        if payform.is_valid():
            obj1=payform.save(commit=False)
            obj1.work = c_work
            obj1.save() 
            c_work.payment_status = 1
            c_work.save()
            return redirect('work_status_view')   
    else:
        payform= paymentForms()
    return render(request,"customer_page/payment.html",{"payform":payform})


    
  
