from django.shortcuts import render,get_object_or_404
from .models import all_blog

def all_blogs(request):
    # images=all_blog.objects.all(),
    blogs = all_blog.objects.order_by('date_published')
    return render(request,'blogspot/all_blogs.html',{'blogs':blogs})

def details(request,blog_id):
    
    blog=get_object_or_404(all_blog,pk=blog_id)
    return render(request,'blogspot/detail.html',{'blog':blog},)
