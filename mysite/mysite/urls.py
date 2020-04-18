from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^rent_company/', include('rent_company.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
