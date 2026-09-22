from django.shortcuts import render

#writing home page view
def home(request):
    return render(request, 'home.html')