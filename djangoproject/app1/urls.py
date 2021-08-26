from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.TestFun,name="test"),
   path('html',views.Fn2,name="html"),
   path('regform',views.RegFun,name="regform"),
]