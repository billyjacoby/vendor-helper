# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.

def blog_home(request):
    content = {'categories': Category.objects.all(),
                'posts': Blog.objects.all().order_by('-posted')[:5],
                }
    return render(request, 'blog/home.html', content)

def view_post(request, slug):
    return render(request, 'blog/view_post.html', {'post': get_object_or_404(Blog, slug=slug)})


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/view_category.html', {'category': category,
                                                'posts': Blog.objects.filter(category=category)[:5]})
