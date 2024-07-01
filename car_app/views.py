from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request,"main_page.html")



def log_in(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        print(user_name)
        user_password = request.POST.get('userpassword')
        print(user_password)
        
        user_click=authenticate(request,username=user_name,password=user_password)
        
        if user_click is not None:
            login(request,user_click)

            if user_click.is_staff:
                return redirect('admin')
            
            elif user_click.is_customer:
                return redirect('customer_page')
            
            elif user_click.is_manager:
                return redirect('manager_page')
        else:
            messages.info(request,'invalid username and password')
    return render(request,"login_page.html")



