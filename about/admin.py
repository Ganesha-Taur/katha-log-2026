from django.contrib import admin
from . models import About, SocialLink
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    #for persmission to add only one about us
    def has_add_permission(self, request):
        #count all about
        count = About.objects.all().count()
        if count ==0:
            return True
        else:
            return False
        
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)