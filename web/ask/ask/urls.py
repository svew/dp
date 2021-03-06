"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse, HttpResponseNotFound

from ask.views import response, notResponse
from qa.views import main, popularQuestions, askFormAction, signupView, loginview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^login/', loginview),
    url(r'^logout/', response),
    url(r'^signup/', signupView),
    url(r'^ask/', askFormAction),
    url(r'^popular/$', popularQuestions),
    url(r'^new/', response),
    url(r'^question/', include('qa.urls')),
    url(r'^', notResponse)
]
