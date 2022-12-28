from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import BookingForm
from .models import Departments,Doctors
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dict_book={
        'form':form
    }
    return render(request,'booking.html',dict_book)
def doctors(request):
    dict__doc ={
        'doctors' : Doctors.objects.all()
    }
    return render(request,'doctors.html',dict__doc)
def contact(request):
   return render(request,'contacts.html')
def department(request):
    dic_dep={ 
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dic_dep)
