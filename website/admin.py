from django.contrib import admin
from website.models import Contact,Newsletter
 # Register your models here.
 
class ContectAdmin(admin.ModelAdmin):
   date_hierarchy = 'created_date'
   list_display=('name','email','created_date')  
   list_filter = ['email']
   search_fields = ['name','messege']
admin.site.register(Contact,ContectAdmin)
admin.site.register(Newsletter)
