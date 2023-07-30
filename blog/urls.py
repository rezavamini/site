from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
path("",views.blog_view,name='index'),
path("single",views.blog_single,name='single'),
]