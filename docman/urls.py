from django.conf.urls import url
from docman import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^accesstype/$', views.AccessTypeList.as_view()),
    url(r'^accesstype/(?P<pk>[0-9]+)/$', views.AccessTypeDetail.as_view()),
    url(r'^documenttype/$', views.documenttype_list),
    url(r'^documenttype/(?P<pk>[0-9]+)/$', views.documenttype_detail),
    url(r'^department/$', views.department_list),
    url(r'^department/(?P<pk>[0-9]+)/$', views.department_detail),
    url(r'^document/$', views.document_list),
    url(r'^document/(?P<pk>[0-9]+)/$', views.document_detail),
    url(r'^role/$', views.role_list),
    url(r'^role/(?P<pk>[0-9]+)/$', views.role_detail),
    url(r'^user/$', views.user_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
]