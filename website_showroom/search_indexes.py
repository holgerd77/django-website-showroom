from haystack import indexes
from website_showroom.models import EditionWebsite

class EditionWebsiteIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return EditionWebsite
