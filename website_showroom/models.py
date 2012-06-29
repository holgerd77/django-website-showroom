import uuid
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import os.path

class Category(models.Model):
    name = models.CharField(max_length=40)
    url_name = models.SlugField(max_length=40, help_text="Every url-conform string except 'contact'")
    order = models.IntegerField(help_text="Numeric value for category order. Tip: Use 100-200-300-... steps for easy reordering.")
    color = models.CharField(max_length=7, help_text="Format: #ffffff")
    active_color = models.CharField(max_length=7, help_text="Format: #ffffff")

    ordering = ['order']

    def __unicode__(self):
        return self.name


def get_path(instance, filename):
    pos = filename.rfind('.')
    path = 'screenshots/' + 's_' + str(uuid.uuid1()) + filename[pos:]
    return path


class Website(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    order = models.IntegerField(help_text="Numeric value for website order. Tip: Use 100-200-300-... steps for easy reordering.")
    help_text = "Optional, 2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site."
    country = models.CharField(max_length=2, null=True, blank=True, help_text=help_text)
    help_text = "Tip: Keep it short, space is limited!"
    desc = models.TextField(help_text=help_text)
    help_text = "Image file, size: 300x200, name will be unified. If you provide a larger file image will be resized (use same proportions, e.g. 600x400 or 750x500)."
    screenshot = models.ImageField(upload_to=get_path, help_text=help_text)
    url = models.CharField(max_length=90)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    ordering = ['category', 'order']

    def __unicode__(self):
        return self.title


@receiver(post_save, sender=Website)
def post_save_handler(sender, instance, using, **kwargs):
    from PIL import Image
    image = Image.open(instance.screenshot)
    print "test"
    print image
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
