from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *


class ListPosts(ListView):
    model = Posts


class CreateViewClass(CreateView):
    model = Posts
    fields = '__all__'


def index(request):
    posts = Posts.objects.all().prefetch_related('comments')
    coms = Comments.objects.all().select_related('user')
    return render(request, 'app/posts_list.html', context={'object_list': posts,
                                                           'coms': coms})


def imageView(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image')
    form = ImageForm()
    images = Image.objects.all()
    return render(request, 'app/form.html', context={'form': form, 'images': images})
