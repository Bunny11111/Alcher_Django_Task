from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'blog/home.html')
def page1(request):
    return render(request,'blog/page1.html')
def page2(request):
    return render(request,'blog/page2.html')