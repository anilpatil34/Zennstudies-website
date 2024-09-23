from urllib import request
from django.shortcuts import render, HttpResponse # type: ignore
from datetime import datetime
from zennapp.models import Contact
from django.contrib import messages # type: ignore

# Create your views here.

def home(request):
    # this is the set of variables context
    context = {
        'variable': "this is variable "
    }

   
    return render(request, 'zennapp/index.html', context)
    # return HttpResponse("hi this is my site")

def about(request):
    return render(request, 'zennapp/About.html')
    # return HttpResponse("hi this is my about")

def services(request):
    return render(request, 'zennapp/Services.html')
    # return HttpResponse("hi this is my services page")

def contact(request):
    # This below code of line we do for user data will be stored succesfully in given sections
    if request.method == "POST":
        # This below is get post method in python
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        # This below line for when user submit his details then this messege will show on contact us page. 
        messages.success(request, "Your form has been send successfully !")
    return render(request, 'zennapp/Contact.html')
    # return HttpResponse("hi this is my Contact")
