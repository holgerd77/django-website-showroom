from django.contrib.syndication.views import Feed
from django.conf import settings
from website_showroom.models import Edition, Website

class RssFeed(Feed):
    eds = Edition.objects.all()
    
    if len(eds) > 0:
        edition = eds[0] 
        title = edition.rss_title
        description = edition.rss_description
    else:
        title = 'RSS Feed'
        description = 'RSS Feed for showroom'
    link = '/rss/'

    def items(self):
        return Website.objects.order_by('-pub_date')[:12]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.url

    def item_description(self, item):
        return item.desc
