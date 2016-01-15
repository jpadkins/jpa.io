from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Article
from .models import Category 

# Create your views here.

def index(request):
    categories = Category.objects.all()
    article = get_object_or_404(Article, pk=1)
    return render(request, 'blog/index.html', {
        'categories': categories,
        'article': article, }
    )

def category(request, category_slug):
    categories = Category.objects.all()
    article = get_object_or_404(Article, pk=1)
    return render(request, 'blog/category.html', {
        'categories': categories,
        'article': article,
        'category_slug': category_slug, }
    )

def article(request, category_slug, article_slug):
    return HttpResponse('This is the page for ' + category_slug
                        + ' and ' + article_slug)
