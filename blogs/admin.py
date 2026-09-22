from django.contrib import admin
from . models import category, Blog
# Register your models here.

#Creating auto generated slug 
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'is_featured')

admin.site.register(category)

admin.site.register(Blog, BlogAdmin)

