from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Ceo,Services,Order,About
from .forms import OrderForm


def home(request):
    ceo = Ceo.objects.all()
    services = Services.objects.all()
    return render(request,"inventory/index.html",{"ceo":ceo,"services":services})

def about(request):
    about = About.objects.all()
    return render(request,"inventory/about_us.html",{"about":about})

def contact(request):
    pass

def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/order_success/")
    else:
        form = OrderForm()
    return render(request,"inventory/order.html",{"form":form})


def order_success(request):
    return render(request,"inventory/order_success.html")