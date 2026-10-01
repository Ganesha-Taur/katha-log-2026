from . models import Category

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories ) #its return all gategories on all pages