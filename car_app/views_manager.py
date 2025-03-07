from django.shortcuts import render,redirect
from .forms import update_working_Forms
from .models import customer_booking,create_work,manager_data
from django.contrib.auth.decorators import login_required


# manager home page
def manager_page(request):
    return render(request,'manager_page/manager.html')

# booking time customer
@login_required(login_url='logIN')
def customer_booking_list(request):
    customer_book_view = customer_booking.objects.all()
    return render(request,'manager_page/customer_booking.html',{'customer_book_view':customer_book_view})

# customer booking approving
@login_required(login_url='logIN')
def status_approved(request,pk):
    customer_book_view = customer_booking.objects.get(pk=pk)
    customer_book_view.status = 1
    customer_book_view.save()
    return redirect('m_v_customer_booking')

# customer booking reject
@login_required(login_url='logIN')
def status_reject(request,pk):
    customer_book_view = customer_booking.objects.get(pk=pk)
    customer_book_view.status = 2
    customer_book_view.save()
    print(customer_book_view)
    return redirect('m_v_customer_booking')

# work view
@login_required(login_url='logIN')
def creat_work_view(request):
    work_user = request.user
    print(work_user)
    work_users = manager_data.objects.get(user= work_user)
    # car_details = customer_booking.objects.get(pk=pk)
    work_view = create_work.objects.filter(Name_manager=work_users)
    return render(request,'manager_page/work_view.html',{'work_view':work_view})

# work update
@login_required(login_url='logIN')
def work_update(request,pk):
    work=create_work.objects.get(pk=pk)
    data = update_working_Forms(instance=work)
    if request.method == 'POST':
        update_work =update_working_Forms(request.POST,instance=work)
        if update_work.is_valid():
            work.save()
            return redirect("work_list")
    return render(request,"manager_page/update_work.html",{"update_work":data})
    
       




