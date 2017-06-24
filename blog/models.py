# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#not sure what this is for
from django.db.models import permalink
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.slug)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_category', None, {'slug': self.slug})

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to="media/images/blog_images/", blank=True )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.slug)
        super(Blog, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})
