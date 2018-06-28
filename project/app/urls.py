from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r'memo', views.MemoViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from app import views
# from django.conf.urls import include
#
# from app.views import MemoViewSet, UserViewSet
# from rest_framework import renderers
#
# memo_list = MemoViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# memo_detail = MemoViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     url(r'^memo$', memo_list, name='memo-list'),
#     url(r'^memo/(?P<pk>[0-9]+)$', memo_detail, name='memo-detail'),
#     url(r'^users$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)$', user_detail, name='user-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
