from django.conf.urls.defaults import patterns, include, url
from website_showroom.feeds import RssFeed

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<ed_country>[-\w]+)/rss/$', RssFeed()), 
    url(r'^search/', include('haystack.urls')),

    url(r'^$', 'website_showroom.views.act_edition_redirect'),
    url(r'^(?P<ed_country>[-\w]+)/$', 'website_showroom.views.index'),
    url(r'^(?P<ed_country>[-\w]+)/contact/', 'website_showroom.views.contact'),
    url(r'^(?P<ed_country>[-\w]+)/(?P<url_name>[-\w]+)/$', 'website_showroom.views.category')
)
