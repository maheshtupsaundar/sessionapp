from django.shortcuts import render
from myapp import forms
from myapp.forms import *
# Create your views here.
def addview(request):
    form=Additemform()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'additem.html',{'form':form})
def displayview(request):
    return render(request,'displayitem.html')