from django.shortcuts import render,redirect

class WelcomeCtl:

    def display(self,request):
        return render(request,'welcome.html')

    def submit(self,request):
        return render(request,'welcome.html')