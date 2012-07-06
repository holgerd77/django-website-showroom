from django.contrib.syndication.views import Feed
from django.conf import settings
from django.shortcuts import get_object_or_404
from website_showroom.models import Edition, EditionWebsite

class RssFeed(Feed):

    title = "Chicagocrime.org site news"
    link = "/rss/"
    description = "Updates on changes and additions to chicagocrime.org."

    def get_object(self, request, ed_country):
        ed = Edition.objects.get(country=ed_country)
        return get_object_or_404(EditionWebsite, edition=ed)

    def items(self):
        return EditionWebsite.objects.order_by('-pub_date')[:12]

    def item_title(self, item):
        return item.get_title

    def item_link(self, item):
        return item.website.url

    def item_description(self, item):
        return item.desc
