from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.filter(status='published').order_by('-published_date')
    return render(request, 'Blogs.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})