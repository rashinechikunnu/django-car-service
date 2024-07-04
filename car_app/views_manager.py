from django.shortcuts import render,redirect
from .forms import ManagerForms,LoginForms,update_working_Forms
from .models import customer_booking,create_work,manager_data


def manager_page(request):

   


    
    return render(request,'manager_page/manager.html')


def customer_booking_list(request):
    customer_book_view = customer_booking.objects.all()
    
    return render(request,'manager_page/customer_booking.html',{'customer_book_view':customer_book_view})

def status_approved(request,pk):
    customer_book_view = customer_booking.objects.get(pk=pk)
    customer_book_view.status = 1
    customer_book_view.save()
    return redirect('m_v_customer_booking')

def status_reject(request,pk):
    customer_book_view = customer_booking.objects.get(pk=pk)
    customer_book_view.status = 2
    customer_book_view.save()
    print(customer_book_view)
    return redirect('m_v_customer_booking')


def creat_work_view(request):
    work_user = request.user
    work_users = manager_data.objects.get( user= work_user)

    work_view = create_work.objects.filter(Name_manager=work_users)
    return render(request,'manager_page/work_view.html',{'work_view':work_view})

def work_update(request,pk):
    work=create_work.objects.get(pk=pk)
    data = update_working_Forms(instance=work)
    if request.method == 'POST':
        update_work =update_working_Forms(request.POST,instance=work)
        if update_work.is_valid():
            work.save()
            return redirect("work_list")

        
    return render(request,"manager_page/update_work.html",{"update_work":data})
    
       




