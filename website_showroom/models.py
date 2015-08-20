import os, uuid
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class Edition(models.Model):
    help_text = "Main title shown on page"
    site_title = models.CharField(max_length=40, help_text=help_text)
    help_text = "2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site."
    country = models.CharField(max_length=2, help_text=help_text)
    help_text = "Numeric value for edition order. Tip: Use 100-200-300-... steps for easy reordering. "
    help_text += "Edition first in order will be used as edition default."
    order = models.IntegerField(help_text=help_text)
    help_text = "Something like 'English version', used for mouseover on flag"
    short_description = models.CharField(max_length=40, help_text=help_text)
    help_text = "Used for html title tag"
    html_title = models.CharField(max_length=100, help_text=help_text)
    help_text = "Subtitle (HTML tags possible)"
    site_subtitle = models.CharField(max_length=125, help_text=help_text)
    help_text = "Title for rss feed"
    rss_title = models.CharField(max_length=100, help_text=help_text)
    help_text = "Description for rss feed"
    rss_description = models.CharField(max_length=200, help_text=help_text)
    help_text = "Optional, link to Facebook page"
    facebook_url = models.CharField(max_length=90, blank=True, null=True, help_text=help_text)
    help_text = "Optional, link to Twitter page"
    twitter_url = models.CharField(max_length=90, blank=True, null=True, help_text=help_text)
    help_text = "Optional, link to Google+ page"
    google_plus_url = models.CharField(max_length=90, blank=True, null=True, help_text=help_text)
    help_text = "Something like - e.g. - 'Home'"
    home_menu_title = models.CharField(max_length=40, help_text=help_text)
    help_text = "HTML color code, e.g. '#999999"
    home_menu_color = models.CharField(max_length=7, help_text=help_text)
    help_text = "HTML color code, e.g. '#000000"
    home_menu_active_color = models.CharField(max_length=7, help_text=help_text)
    help_text = "Number of websites for home category"
    home_num_websites = models.IntegerField(help_text=help_text)
    help_text = "Left footer (HTML tags possible)"
    footer_left = models.CharField(max_length=200, help_text=help_text)
    help_text = "Right footer (HTML tags possible)"
    footer_right = models.CharField(max_length=200, help_text=help_text)
    help_text = "Title of contact navi"
    contact_title = models.CharField(max_length=40, help_text=help_text)
    help_text = "Complete HTML content of contact page, with <p>, <br> and all that stuff"
    contact_html = models.TextField()
    comments = models.TextField(blank=True)
    
    ordering = ['order']
    
    def __unicode__(self):
        return self.site_title + " (" + self.country + ")"


class Category(models.Model):
    help_text = "Only used in admin context, not displayed on site (edition specific category names)"
    name = models.CharField(max_length=40, help_text=help_text)
    color = models.CharField(max_length=7, help_text="Format: #ffffff")
    active_color = models.CharField(max_length=7, help_text="Format: #ffffff")

    def __unicode__(self):
        return self.name

    def get_ed_categories(self):
        return EditionCategory.objects.filter(category_id=self.id)
    
    def editions(self):
        ed_categories = self.get_ed_categories()
        ret = ''
        for ed_c in ed_categories:
            if len(ret) > 0:
                ret += ' | '
            ret += ed_c.edition.country
        return ret


class EditionCategory(models.Model):
    edition = models.ForeignKey(Edition)
    category = models.ForeignKey(Category)
    help_text = "Edition specific category name"
    name = models.CharField(max_length=40, help_text=help_text)
    help_text = "Every url-conform string except 'contact' (e.g. 'my-category-1')"
    url_name = models.SlugField(max_length=40, help_text=help_text)
    help_text = "Numeric value for category order. Tip: Use 100-200-300-... steps for easy reordering."
    order = models.IntegerField(help_text=help_text)
    
    ordering = ['order']


def get_path(instance, filename):
    pos = filename.rfind('.')
    path = 'screenshots/' + 's_' + str(uuid.uuid1()) + filename[pos:]
    return path

class Website(models.Model):
    help_text = "Generic title, used if no extra edition specific title is provided"
    title = models.CharField(max_length=50, help_text=help_text)
    category = models.ForeignKey(Category)
    help_text = "Optional, 2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site."
    country = models.CharField(max_length=2, null=True, blank=True, help_text=help_text)
    help_text = "Image file, size: 300x200, name will be unified. "
    help_text += "Larger file image will be resized. "
    help_text += "Greater height will be cropped (making screen capture with website width "
    help_text += "and height generously higher than aspect ratio is easiest)"
    screenshot = models.ImageField(upload_to=get_path, help_text=help_text)
    url = models.CharField(max_length=90)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    ordering = ['category']

    def __unicode__(self):
        return self.title
    
    def get_ed_websites(self):
        return EditionWebsite.objects.filter(website_id=self.id)

    def editions(self):
        ed_websites = self.get_ed_websites()
        ret = ''
        for ed_ws in ed_websites:
            if len(ret) > 0:
                ret += ' | '
            ret += ed_ws.edition.country + ' (' + str(ed_ws.order) + ')'
        return ret


@receiver(post_save, sender=Website)
def post_save_handler(sender, instance, using, **kwargs):
    from PIL import Image
    image = Image.open(instance.screenshot)
    thumb_ratio = float(1.5)
    img_ratio = float(image.size[0]) / float(image.size[1])
    print "Ratios: T " + str(thumb_ratio) + ", I " + str(img_ratio)
    # img is relatively heigher than thumb
    if thumb_ratio > img_ratio:
        crop_width = image.size[0]
        crop_height = int(image.size[0] / thumb_ratio)
        image = image.crop((0, 0, crop_width, crop_height,))
    image.thumbnail([300, 200], Image.ANTIALIAS)
    image.save(settings.MEDIA_ROOT + '/' + instance.screenshot.name)
    

@receiver(pre_delete, sender=Website)
def pre_delete_handler(sender, instance, using, **kwargs):
    try:
        path = settings.MEDIA_ROOT + '/' + instance.screenshot.name
        os.remove(path)
    except OSError:
        pass

pre_delete.connect(pre_delete_handler, sender=Website)
post_save.connect(post_save_handler, sender=Website)


class EditionWebsite(models.Model):
    edition = models.ForeignKey(Edition)
    website = models.ForeignKey(Website)
    help_text = "Edition specific title, if left empty, generic title is used"
    title = models.CharField(max_length=50, null=True, blank=True, help_text=help_text)
    help_text = "Edition specific description"
    desc = models.TextField(help_text=help_text)
    help_text = "Numeric value for website order. Tip: Use 100-200-300-... steps for easy reordering."
    order = models.IntegerField(help_text=help_text)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    
    def get_title(self):
        if self.title:
            return self.title
        else:
            return self.website.title
