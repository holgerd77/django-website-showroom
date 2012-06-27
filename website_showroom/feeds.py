from django.contrib.syndication.views import Feed
from django.conf import settings
from website_showroom.models import Website

class RssFeed(Feed):
    title = settings.RSS_TITLE
    link = '/rss/'
    description = settings.RSS_DESCRIPTION

    def items(self):
        return Website.objects.order_by('-pub_date')[:12]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.url

    def item_description(self, item):
        return item.desc
