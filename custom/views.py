from django.shortcuts import render,redirect
from .models import *


def dashboard(request):
    categories = Order.objects.all()
    return render(request,'index.html',{'categories': categories})



def home(request):
    return render(request,'index2.html')



def order(request):
    if request.method == "POST":
        data = request.POST
        name= data.get('name')
        slug = data.get('slug')
        image = request.FILES.get('image')
        
        
        Order.objects.create(
            name = name,
            slug = slug,
            image = image,
            )
        
       
        return redirect ("/admin/order/")

    abc = Order.objects.all()
    context = {'abc': abc}
    return render(request, 'category.html', context) 




def product(request):
    xyz = Order.objects.all()
    return render(request,'product.html',{'xyz': xyz})



def update(request,id):   
    queryset = Order.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        image= request.FILES.get('image')
        name = data.get('name')
        slug= data.get('slug')

        queryset.name = name
        queryset.slug = slug

        if image:
            queryset.image = image

        queryset.save()
        return redirect ("/admin/order/")

    context = {'order': queryset}

    return render (request,"update.html", context)


def delete(request,id):
    queryset = Order.objects.get(id = id)
    queryset.delete()
    return redirect ("/admin/order/")