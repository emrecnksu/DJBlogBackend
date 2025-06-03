# frontend/views.py

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Category, Post, Comment

def home(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'frontend/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    comments = Comment.objects.filter(post=post, is_approved=True).order_by('-created_at')
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'frontend/post_detail.html', context)

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(is_published=True, categories=category).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'current_category': category,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'frontend/category_posts.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        Comment.objects.create(
            post=post,
            author=request.user,
            email=request.user.email,
            content=content,
            is_approved=True
        )
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
