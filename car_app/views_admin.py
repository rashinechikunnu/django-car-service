from django.shortcuts import render,redirect
from .models import Feedback, manager_data,Customer_data,shedules
from .forms import ManagerForms,LoginForms,sheduleForm

# admin page

def admin_page(request):
    return render(request,"admin_page/admin.html")




# manager account creation page

def manager_create_page(request):

    mang1 = LoginForms()
    mang2 = ManagerForms()
    
    if request.method == "POST":
        
        mang1 = LoginForms(request.POST)
        
        mang2 = ManagerForms(request.POST)
        
        
        if mang1.is_valid() and mang2.is_valid():
            a = mang1.save(commit=False)
            a.is_manager = True
            a.save()
            
            user1= mang2.save(commit=False)
            user1.user=a
            user1.save()
            
            return redirect('admin')

   

    return render(request,"admin_page/managers_create.html",{'mang1': mang1,'mang2': mang2})


# manager data list

def list_managers(requst):
    list_manager = manager_data.objects.all()
    return render(requst,'admin_page/list_manager.html',{'list_manager':list_manager})


# manager data editing

def edit_manager(request,pk):

    edt = manager_data.objects.get(pk=pk)
    
    if request.method == 'POST':
        frm = ManagerForms(request.POST,request.FILES,instance=edt)
        if frm.is_valid():
            edt.save()
            return redirect('list_of_manager')

    else:
        frm = ManagerForms(instance=edt)

    return render(request,'admin_page/edit.html',{'frm':frm})



# manager data delete

def deleted(request,pk):
    manager_delete=manager_data.objects.get(pk=pk)
    manager_delete.delete()
    list_manager=manager_data.objects.all()

    return render(request,'admin_page/list_manager.html',{'list_manager':list_manager})




# customer area

def customer_data_list(request):
    custm_data_list = Customer_data.objects.all()

    return render(request,'admin_page/customer_list.html',{'custm_data_list':custm_data_list})



def delete_customer_data(request,pk):
    customer_delete=Customer_data.objects.get(pk=pk)
    customer_delete.delete()
    return redirect('list_of_customer')
    
    

def feedback_customer(request):
    
    feedback_customer_list = Feedback.objects.all() 
    
    return render(request,'admin_page/feedback_customer.html',{'fdb_customer':feedback_customer_list})



def replay_cunstomer(request,pk):
    rply =Feedback.objects.get(pk=pk)

    
    if request.method == 'POST':
        rplyfrm = request.POST.get('replaaay')
        rply.replay=rplyfrm
        rply.save()
        return redirect('customer_feedback')
    
    return render(request,'admin_page/customer_replay.html',{'rply':rply})


def shedule_add(request):
    if request.method == 'POST':
        data = sheduleForm(request.POST)
        print(data)
        if data.is_valid():
            data.save()
            return redirect('schedule_views')
    else:
        data = sheduleForm() 
    return render(request,"admin_page/shedule.html",{"shd":data})

def schedule_list(request):
    schedule_views=shedules.objects.all()
    return render(request,'admin_page/schedule_view.html',{'schedule_views':schedule_views})

def schedule_delete(request,pk):
        delt=shedules.objects.get(pk=pk)
        delt.delete()
        return redirect('schedule_views')
        

    
    
         

