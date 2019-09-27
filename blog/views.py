from django.shortcuts import render
from .models import Blog

def myblog(request):
    blog = Blog.objects
    return render(request, 'blog/myblog.html', {'blog': blog})