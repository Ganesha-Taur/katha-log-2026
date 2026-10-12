from django.shortcuts import render
from blogs.models import Category, Blog
from about.models import About
#writing home page view
def home(request): 
    #featured posts on homepage
    featured_posts = Blog.objects.filter(is_featured=True, status = 'Published').order_by('updated_at')
    #for display normal or recent article
    posts = Blog.objects.filter(is_featured=False, status = 'Published')

    #fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    
    
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about
    }
    return render(request, 'home.html', context)