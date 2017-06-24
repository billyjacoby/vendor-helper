# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class SiteNewsPage(TemplateView):
    template_name = "blog/home_list.html"

    def get_context_data(self, **kwargs):
        context = super(SiteNewsPage, self).get_context_data(**kwargs)
        context['object_list'] = Blog.objects.filter(category__title__iexact='News')[:10]
        context['subject'] = "News"
        return context

class ArticleDetail(DetailView):
    model = Blog
    template_name = 'blog/view_post.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['subject'] = context['object'].category.title
        return context

class BlogHome(ListView):
    template_name = "blog/home_list.html"
    model = Blog

class CategoryHome(ListView):
    template_name = "blog/category_list.html"
    model = Category

class CategorySingle(TemplateView):
    template_name = "blog/home_list.html"

    def get_context_data(self, **kwargs):
        context = super(CategorySingle, self).get_context_data(**kwargs)
        slug = kwargs.get('slug')
        context['object_list'] = Blog.objects.filter(category__slug=slug)
        context['subject'] = slug.title()
        return context
