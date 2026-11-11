from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from about.models import About
from . forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
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

# register functionality
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

#login 
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html',context)

#logout 
def logout(request):
    auth.logout(request)
    return redirect('home')