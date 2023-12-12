from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def order(request):
    return render(request, 'orders/order.html')