"""titicom URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from home import views as home_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^estore/', include('estore.urls', namespace='estore')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)