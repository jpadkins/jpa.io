from django.shortcuts import render 
from .models import Article
from .models import Category
from .models import Tag

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')
