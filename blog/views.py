from django.shortcuts import render,get_object_or_404
from blog.models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    blogdict = {
        'blogs':blogs,
    }
    return render(request, 'blog/blog.html', context=blogdict)
    
def blogdetail(request,blog_id):
    detail = get_object_or_404(Blog, pk=blog_id) #detail = Blog.objects.get(pk=blog_id)
    # print(detail)
    context = {
        'detail':detail
    }
    return render(request,'blog/blogdetail.html',context)