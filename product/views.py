from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

def productDetail(request,id):
    product=Product.objects.get(id=id)
    return render(request, 'product_detail.html',{'product':product})