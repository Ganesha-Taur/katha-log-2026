from django.shortcuts import render
from blogs.models import Category, Blog
#writing home page view
def home(request): 
    #featured posts on homepage
    featured_posts = Blog.objects.filter(is_featured=True, status = 'Published').order_by('updated_at')
    #for display normal or recent article
    posts = Blog.objects.filter(is_featured=False, status = 'Published')
    
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)