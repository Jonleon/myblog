"""My_Page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog.views import index,me,mywork,blog,artical,journey
from django.conf.urls.static import static
from django.conf import settings
from DjangoUeditor import urls as djud_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',index,name = 'index'),
    url(r'^me/', me, name='me'),
    url(r'^mywork/', mywork, name='mywork'),
    url(r'^blog/', blog, name='blog'),
    url(r'^artical/', artical, name='artical'),
    url(r'^',include('blog.urls',namespace='blog')),
    url(r'^journey/', journey, name='journey'),
    url(r'^ueditor/',include(djud_urls)),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)