from django.shortcuts import render

# Create your views here.

# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse

from datetime import datetime
from myapp.models import Contact,Employee
from django.contrib import messages
from django.template import loader  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myapp.forms import EmployeeForm
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
  

def index(request):  
   template = loader.get_template('max.htm') # getting our template  
   return HttpResponse(template.render())       # rendering the template in HttpResponse  


def about(request):
   max= loader.get_template('max.htm') # getting our template  
   return HttpResponse(max.render())       # rendering the template in HttpResponse  



def services(request):
    
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       desc = request.POST.get('desc')
       rai=Contact(name=name,email=email,phone=phone,desc=desc,
       date=datetime.today())
       rai.save()
       messages.success(request,'your message have been collected in our databaase ☢☢')

    return render(request,"services.htm")       # rendering the template in HttpResponse  




def condition(request):
   condition = loader.get_template('condition.htm') # getting our template  
   return HttpResponse(condition.render())       # rendering the template in HttpResponse  

def register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if Employee.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return  redirect('register')
            elif Employee.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return  redirect('register')    
            
            ######################### mail system ####################################
            else:
                form.save()
                htmly = get_template('Email.htm')
                d = { 'username': username }
                subject, from_email, to = 'welcome', 'your_email@gmail.com', email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            ##################################################################
                messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')

            
    else:
        form = EmployeeForm()
    return render(request, 'register.htm', {'form': form, 'title':'reqister here'})
def show(request):  
    employees = Employee.objects.all()  
   
    return render(request,"show.htm",{'employees':employees,})  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
           messages.info(request, f'account done not exit plz sign up')
    form = AuthenticationForm()
    return render(request, 'login.htm', {'form':form, 'title':'log in'})
  

def show(request):  
    employee = Employee.objects.all()  
    return render(request,'show.htm', {'employee':employee}) 