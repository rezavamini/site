from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.utils import timezone

def blog_view(request,**kwargs):
    corrent_time = timezone.now()
    Posts = Post.objects.filter(published_date__lte=corrent_time,status = 1)
    #فیلتر بر اساس کتگوری
    if kwargs.get('cat_name') != None:
      Posts = Posts.filter(category__name = kwargs['cat_name'] )
      #فیلتر بر استاس نویسنده
    if kwargs.get('author_username') != None:
      Posts = Posts.filter(author__username = kwargs['author_username'])
    context = {'Posts': Posts}
    return render(request,"blog/blog-home.html",context)

def blog_single(request,pid):
    #باید به عرض برسونم که چیزی جز این روش به ذهنم نرسید ولی واقعا دیگه نمیدونم مشکل کجاست با تشکر
       #  پست فعلی
    #current_post = Post.objects.get(id=pid)

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

def blog_category(request,cat_name):
  posts = Post.objects.filter(status = 1)
  posts = posts.filter(category__name = cat_name )
  context = {'Posts': posts}
  return render(request,'blog/blog-home.html',context)

def blog_search(request):
 corrent_time = timezone.now()
 Posts = Post.objects.filter(published_date__lte=corrent_time,status = 1)
 if request.method == 'GET':
   if s := request.GET.get('s'):
    Posts = Posts.filter(content__contains = s)
 context = {'Posts': Posts}
 return render(request,"blog/blog-home.html",context)