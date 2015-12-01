from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'blog.blogapp.views.index'),
                       url(r'^update/', 'blog.blogapp.views.update'),
                       url(r'^delete/', 'blog.blogapp.views.delete'),
                       )
