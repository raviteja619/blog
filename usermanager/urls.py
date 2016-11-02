from django.conf.urls import include, url
from django.contrib import admin
from . import views
from . import api

urlpatterns = [
    # Api Urls
    url(r'^api-v1/users/', api.UserList.as_view(), name="user_api"),
    url(r'^api-v1/user/(?P<term>[-\w]+)/', api.UserQuery.as_view(), name="userdetails_api"),
]
