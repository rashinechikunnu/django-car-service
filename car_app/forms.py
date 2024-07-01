from .models import Login,Customer_data,manager_data,Feedback,shedules,customer_booking
from django import forms
from django.contrib.auth.forms import UserCreationForm
 
# create a login ModelForm

class LoginForms(UserCreationForm):
    # specify the name of model to use
    username=forms.CharField()
    password1=forms.CharField(label="password", widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password2=forms.CharField(label="password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields =('username',"password1","password2") 


# create a customer_data modelForm

class CustomerForms(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Customer_data
        fields ="__all__"
        exclude = ("user",)



# create a manager_data modelForm

class ManagerForms(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = manager_data
        fields ="__all__"
        exclude = ("user",)


# feedback form

class feedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('text_me'),


# time schedule form

class dateinput(forms.DateInput):
    input_type='date'

class timeinput(forms.TimeInput):
    input_type = 'time'



class sheduleForm(forms.ModelForm):
    date = forms.DateField(widget=dateinput)
    starting_time=forms.TimeField(widget=timeinput)
    ending_time=forms.TimeField(widget=timeinput)
    class Meta:
        model = shedules
        fields = ('date','starting_time','ending_time')


# customer booking
class Customer_booking_Forms(forms.ModelForm):
   
    class Meta:
        model = customer_booking
        fields ="__all__"
        exclude = ("user","schedule","status")




     