from django.shortcuts import render

from .models import Post

#
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug): # написали slug, потому что в файле urls в path мы ждём slug
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})