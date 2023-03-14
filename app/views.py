from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'GANESH','age':23}
    return render(request,'first.html',context=d)
