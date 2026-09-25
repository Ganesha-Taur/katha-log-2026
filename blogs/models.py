from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#category model
class category(models.Model):
    category_name = models.CharField(max_length=50, unique=True) #unique use for at a time one catetory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name_plural = 'Categories'

    #str reprentor of category model
    def __str__(self):
        return self.category_name

#Drop down for status presend in blog model

STATUS_CHOISES = (
    ('Draft', 'Draft'),
    ('Published', 'Published')
)

#Blog Model
class Blog(models.Model):
    title = models.CharField(max_length= 100)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='upload/%Y/%m/%d')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=30,choices=STATUS_CHOISES, default= 'Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #str repentor of blog model
    def __str__(self):
        return self.title
