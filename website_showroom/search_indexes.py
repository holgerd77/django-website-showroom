from haystack import indexes
from website_showroom.models import Website

class WebsiteIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Website
