from django.contrib import admin
from blog.models import Post,Category
# Register your models here.

class postadmin(admin.ModelAdmin):
 date_hierarchy = "created_date"
 empty_value_display = "-empty-"  
 list_display = ("title",'author','created_date',"counted_view","status","published_date")
 list_filter = ["status",'author',"category"]
 search_fields = ['title','content']
 
admin.site.register(Category)
admin.site.register(Post,postadmin)

