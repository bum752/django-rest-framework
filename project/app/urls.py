from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from django.conf.urls import include

urlpatterns = [
    url(r'^memo$', views.MemoList.as_view()),
    url(r'^memo/(?P<pk>[0-9]+)$', views.MemoDetail.as_view()),
    url(r'^users$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
