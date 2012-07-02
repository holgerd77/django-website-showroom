from django.contrib.syndication.views import Feed
from django.conf import settings
from website_showroom.models import Edition, Website

class RssFeed(Feed):
    edition = Edition.objects.all()[0]
    
    title = edition.rss_title
    link = '/rss/'
    description = edition.rss_description

    def items(self):
        return Website.objects.order_by('-pub_date')[:12]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.url

    def item_description(self, item):
        return item.desc
