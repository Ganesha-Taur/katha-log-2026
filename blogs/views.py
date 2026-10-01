from django.shortcuts import render, redirect

from . models import Category, Blog 

# Create your views here.
def posts_by_category(request, category_id):
    #featch the posts that are published and category should match with request
    posts = Blog.objects.filter(status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        #redirect the user to homepage when category does not exist
        return redirect('home')
    context = {
        'posts': posts,
        'category': category,
    }
    return render (request, 'post_by_category.html', context)
    