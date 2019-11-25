from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def allblogs(request):
    blog_entry = Blog.objects #call Blog Objects
    return render(request, 'blog/allblogs.html', {'blog':blog_entry}) #show those ojects on blog/allblogs.html


def details(request, blog_id):
   details_entry =  get_object_or_404(Blog, pk=blog_id)
   return render(request, 'blog/details.html', {'detail':details_entry})