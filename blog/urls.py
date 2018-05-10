from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.artical, name='product_list'),
    url(r'^(?P<id>\d+)/$',
        views.artical,
        name='artical_by_name'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.artical,
        name='product_detail'),
    ]