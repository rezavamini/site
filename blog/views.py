from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    corrent_time = timezone.now()
    Posts = Post.objects.filter(published_date__lte=corrent_time,status = 1)
    context = {'Posts': Posts}
    return render(request,"blog/blog-home.html",context)

def blog_single(request,pid):
    #جمع کردن ویو 
    post = Post.objects.get(id=pid)
    post.counted_view += 1
    post.save()
    #
    corrent_time = timezone.now()
    post = get_object_or_404(Post,pk=pid,published_date__lte=corrent_time,status = 1)
    context = {'post':post}
    return render(request,"blog/blog-single.html",context)

def test(request):
    return render(request,'test.html')