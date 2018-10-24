from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Home.html')
def link(request):
    return render(request,'Linked.html')