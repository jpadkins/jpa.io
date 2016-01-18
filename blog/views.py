from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import Article
from .models import Category 

# Create your views here.

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'blog/index.html', {
        'categories': categories,
        'articles': articles, }
    )

def category(request, category_slug):
    categories = Category.objects.all() 
    current_category = [a for a in Category.objects.all() if a.slug() == category_slug][0]
    articles = [a for a in Article.objects.order_by('-pub_date')[:10] if slugify(a.category) == category_slug] 
    return render(request, 'blog/category.html', {
        'categories': categories,
        'current_category': current_category,
        'articles': articles,
        'category_slug': category_slug,} 
    )

def article(request, category_slug, article_slug):
    categories = Category.objects.all()
    article = [a for a in Article.objects.all() if slugify(a.title) == article_slug][0]
    return render(request, 'blog/article.html', {
        'categories': categories,
        'article': article,
        'category_slug': category_slug,} 
    )
