from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<category_slug>[\w-]+)/$', views.category, name='category'),
    url(r'^blog/(?P<category_slug>[\w-]+)/(?P<article_slug>[\w-]+)/$', views.article, name='article'),
]
