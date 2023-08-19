from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    corrent_time = timezone.now()
    Posts = Post.objects.filter(published_date__lte=corrent_time,status = 1)
    context = {'Posts': Posts}
    return render(request,"blog/blog-home.html",context)

def blog_single(request,pid):
    #باید به عرض برسونم که چیزی جز این روش به ذهنم نرسید ولی واقعا دیگه نمیدونم مشکل کجاست با تشکر
       #  پست فعلی
    current_post = Post.objects.get(id=pid)

    #  پست قبلی
   # try:
      #  previous_post = Post.objects.filter(id__lt=pid).latest('id')
   # except Post.DoesNotExist:
      #  previous_post = None

    #  پست بعدی
    #try:
      #  next_post = Post.objects.filter(id__gt=pid).earliest('id')
    #except Post.DoesNotExist:
      #  next_post = None
    
    post = get_object_or_404(Post,id=pid)
    
   
     #جمع کردن ویو 
    post.counted_view += 1
    post.save()
    
    corrent_time = timezone.now()
    post = get_object_or_404(Post,pk=pid,published_date__lte=corrent_time,status = 1)
    context = {'post':post,
               #'current_post': current_post,
        #'previous_post': previous_post,
        #'next_post': next_post
              
        
        }
    return render(request,"blog/blog-single.html",context)

def test(request):
    return render(request,'test.html')