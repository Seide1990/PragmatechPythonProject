from django.http import request
from django.shortcuts import render
from .models import Blog     #blog tablesinden data goturmek ucun



# Create your views here.
def index(request):
    
    return render(request,'index.html')
def blog_list(request):
    blogs=Blog.objects.all()   #databaseden datani secdik
 
    content={'blogs':blogs}
    return render(request,'blogs.html',content)
def about(request):
    return render(request,'about.html')
def blog_detail(request,id):

    return render(request,'blog-detail.html')


