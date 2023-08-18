from django.contrib import admin
from blog.models import Post
# Register your models here.

class postadmin(admin.ModelAdmin):
 date_hierarchy = "created_date"
 empty_value_display = "-empty-"  
 list_display = ("title",'author','created_date',"counted_view","status","published_date")
 list_filter = ["status",'author']
 search_fields = ['title','content']
 

admin.site.register(Post,postadmin)

