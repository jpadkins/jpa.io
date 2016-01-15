from django.db import models
from django.conf import settings

"""
The 'article' model contains information for an individual
blog post, including a title, body markdown, date published,
whether or not it is a draft, and the filepath of the 
thumbnail image.
"""
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    is_draft = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=settings.BLOG_IMAGES_DIR
        + 'articles/')
    category = models.ForeignKey(
        'category',
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField('tag')

"""
The 'category' model contains a single data field that is the
name of the category. Category objects are used for generating
sidebar tabs and for sorting purposes.
"""
class Category(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to=settings.BLOG_IMAGES_DIR
    + 'articles/')

"""
The 'tag' model is similar to the category model above, except
tags are meant to be attached in bulk as appropriate to articles,
whereas an article would fall under only one category.
"""
class Tag(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to=settings.BLOG_IMAGES_DIR
    + 'articles/')
