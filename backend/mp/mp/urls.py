"""mp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from api.v1.item.views import SchoolViewSet
from mp.settings import MEDIA_ROOT

router = DefaultRouter()
router.register('v1/school', SchoolViewSet, basename='school')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    #文件
    path('media/<path:path>', serve, {'document_root':MEDIA_ROOT}),
    #drf文档，title自定义
    path('docs',include_docs_urls(title='应心APIdoc')),

    #drf url
    path('', include(router.urls)),
]
