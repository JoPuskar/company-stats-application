"""companystatsviz URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import settings

from companystats import urls as companystats_urls

from companystats import routers as companystats_router

api_urlpatterns = [
	url(r'', include(companystats_router.router.urls))
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^companystats/', include(companystats_urls)),
    url(r'^api/', include(api_urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
