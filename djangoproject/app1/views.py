from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('function is working')
def Fn2(request):
    return render(request,'login.html') 
def RegFun(request):
    return render(request,'registration.html')
