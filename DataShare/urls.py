"""DataShare URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from App import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^logval',views.logval,name="logval"),
    url(r'^vb',views.vb,name="vb"),
    url(r'^dataownlog',views.dataownlog,name="dataownlog"),
    url(r'^approved',views.approved,name="approved"),#
    url(r'^otherslog',views.otherslog,name="otherslog"),
    url(r'^loginval',views.loginval,name="loginval"),
    url(r'^cloudpage',views.cloudpage,name="cloudpage"),
    url(r'^inbpage',views.inbpage,name="inbpage"),
    url(r'^newadmin',views.newadmin,name="newadmin"),
    url(r'^signup',views.signup,name="signup"),
    url(r'^data',views.data,name="data"),
    url(r'^duvalu',views.duvalu,name="duvalu"),
    url(r'^duind',views.duind,name="duind"),
    url(r'^ind',views.ind,name="ind"),
    url(r'^dq1',views.dq1,name="dq1"),
    url(r'^dq2',views.dq2,name="dq2"),
    url(r'^valu',views.valu,name="valu"),
    url(r'^download',views.download,name="download"),
    url(r'^sen',views.sen,name="sen"),
    url(r'^newsen',views.newsen,name="newsen"),
    url(r'^log',views.log,name="log"),
    url(r'^sig',views.sig,name="sig"),
    url(r'^verify',views.verify,name="verify"),
    url(r'^reqfile',views.reqfile,name="reqfile"),
    url(r'^deprole',views.deprole,name="deprole"),
    url(r'^selected',views.selected,name="selected"),
    url(r'^accesspolicy',views.accesspolicy,name="accesspolicy"),
    url(r'^saving',views.saving,name="saving"),
]
