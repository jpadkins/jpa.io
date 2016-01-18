from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /programming/
    url(r'^blog/(?P<category_slug>[\w-]+)/$', views.category, name='category'),
    # ex: /programming/how-i-made-this-website
    url(r'^blog/(?P<category_slug>[\w-]+)/(?P<article_slug>[\w-]+)/$', views.article, name='article'),
]
