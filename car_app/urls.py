from django.urls import path
from . import views,views_admin,views_customer,views_manager

urlpatterns = [
    # main page
    path("",views_customer.customer_account_creation,name=""),
    # login page
    path("login",views.log_in,name='logIN'),
    # admin page
    path("admin_page",views_admin.admin_page,name="admin"),
    # customer page
    path("customer",views_customer.customer_page,name="customer_page"),
    # manager page
    path("manager",views_manager.manager_page,name="manager_page"),
    # logout
    path('log_out',views.log_out,name='log_out'),
    

    # admin area
    # create manager account
    path("manager_creation",views_admin.manager_create_page,name="manager_creation"),
    # view managers list
    path('list_manager',views_admin.list_managers,name='list_of_manager'),
    # edit managers
    path('edit/<pk>',views_admin.edit_manager,name='views_change'),
    # delete managers
    path('delete/<pk>',views_admin.deleted,name='delete_manager_data'),
    # view customer feedback
    path('customer_feedback',views_admin.feedback_customer,name='customer_feedback'),
    # replay customer feedback
    path('replay_to_customer/<pk>',views_admin.replay_cunstomer,name='replay_customer'),
    # view customers list
    path('list_customer',views_admin.customer_data_list,name='list_of_customer'),
    # delete customers
    path('customer_delete/<pk>',views_admin.delete_customer_data,name='delete_customer_data'),
    # view schedule
    path('schedule_views',views_admin.schedule_list,name='schedule_views'),
    # admin shedule
    path('customer_shedule',views_admin.shedule_add,name='customer_schedule'),
    # delete schedule
    path('schedule_delete/<pk>',views_admin.schedule_delete,name='schedule_delete'),
    # approved booking customer
    path('apporved_customers',views_admin.view_approved_customer,name='apporved_customers'),
    #add manager booking customer
    path('admin_add_managers_for_working/<pk>',views_admin.create_workers,name='admin_add_managers_for_working'),
    # work_status_view
    path('show_working',views_admin.working_status_show,name='show_working'),
   
   
    # customer area
    # add feedback
    path('feedback',views_customer.feedback_customer,name='feedback'),
    # view feedback
    path('feedback_views',views_customer.feedback_view,name='feedback_views'),
    # view booking time
    path('schedule_time_view',views_customer.schedule_time,name='view_schedule'),
    # booking customer
    path('book_customer/<pk>',views_customer.booking_customer,name='customers_booking'),
    # view booking status
    path('book_views',views_customer.booking_views,name='booking_list'),
    # customer work status
    path('work_status_view',views_customer.work_status,name="work_status_view"),
    # payment
    path('payments/<pk>',views_customer.payment,name='payments'),



    # manager area
    path('manager_views_customer_booking',views_manager.customer_booking_list,name='m_v_customer_booking'),
    # manager accept / reject
    path('manager_approved/<pk>',views_manager.status_approved,name='approved_manager'),
    path('manager_rejected/<pk>',views_manager.status_reject,name='rejected_manager'),
    #show worikig list
    path('work list',views_manager.creat_work_view,name="work_list"),
    # manager update work
    path('update_work/<pk>',views_manager.work_update,name='update_work'),


]
