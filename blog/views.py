from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date') # [:3] # the most current ones will pop up and to limit the no of blogs inside [:number]
    return render(request, 'blog/all_blogs.html' , {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request , 'blog/detail.html', {'blog': blog})
