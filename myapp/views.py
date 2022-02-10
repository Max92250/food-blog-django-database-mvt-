from django.shortcuts import render

# Create your views here.

# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse

from datetime import datetime
from myapp.models import Services
from django.contrib import messages

def index(request) :

   context = {
     'max':'my name is max chamling rai'
    }

   return render(request, "max.htm",context)



def about(request):
     return render(request, "max.htm")


def services(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       desc = request.POST.get('desc')
       max=Services(name=name,email=email,phone=phone,desc=desc,
       date=datetime.today())
       max.save()
       messages.success(request,'your message have been collected in our databaase ☢☢')

    return render(request, "services.htm")


def condition(request):
     return render(request, "condition.htm")


  

