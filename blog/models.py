from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

"""
The 'article' model contains information for an individual
blog post, including a title, body html, date published,
whether or not it is a draft. 
"""
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    is_draft = models.BooleanField(default=True) 
    category = models.ForeignKey(
        'category',
        on_delete=models.CASCADE,
    )

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

"""
The 'category' model contains a data field that is the name of 
the category and a slug. Category objects are used for generating
sidebar tabs and for sorting purposes.
"""
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
   
    def slug(self):
        return slugify(self.name)
    
    def __str__(self):
        return self.name
