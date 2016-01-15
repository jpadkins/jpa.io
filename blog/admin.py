from django.contrib import admin
from .views import Category
from .views import Article

# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
