from django.shortcuts import render
from blog.models import BlogPost, Tag, Category

def home_view(request):
    posts = BlogPost.objects.filter(is_active=True) #.order_by('-created_at')
    tags = Tag.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    context = dict(
        posts=posts,
        tags = tags,
        categories = categories,
    )
    return render(request, 'page/home_page.html', context)