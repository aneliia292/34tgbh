from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *

def index(request):
    products = Products.objects.all()
    return render(request, 'shop/products_list.html', context={'object_list': products})


def imageView(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image')
    form = ImageForm()
    images = Products.objects.all()
    return render(request, 'shop/index.html', context={'form': form, 'images': images})


