from django.conf.urls import patterns, include, url
from . import api
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^blogs/new/$', views.NewBlogView.as_view(),
        name="add_new_blog"),
    url(r'^blogs/all/$', views.BlogView.as_view(),
        name="all_prezi"),
    url(r'^blog-summary/$', views.get_blog_summary,
        name="get_blog_summary"),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.get_blog_summary,
        name="open_blog_summary"),
    url(r'^blog/edit/(?P<slug>[-\w]+)/$', views.edit_blog,
        name="edit_blog"),

    # API URLs
    url(r'^api-v1/blogs/$', api.BlogView.as_view(),
        name="blogs_api"),
    url(r'^api-v1/blog/delete/(?P<pk>\d+)/',
        api.BlogView.as_view(), name='delete_blog'),
    url(r'^api-v1/blog/(?P<pk>[-\w]+)/',
        api.BlogDetails.as_view(), name="blog_api"),
    url(r'^api-v1/search/blog/',
        api.SearchBlog.as_view(), name="search_blog_api"),
)
