from django.shortcuts import render

# Create your views here.

# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse

from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.template import loader  

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


  

