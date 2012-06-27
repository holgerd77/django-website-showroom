from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from website_showroom.models import Category, Website

def get_home_dummy_cat():
    cat = Category()
    cat.name = settings.HOME_MENU_TITLE
    cat.url_name = ''
    cat.color = settings.HOME_MENU_COLOR
    cat.active_color = settings.HOME_MENU_ACTIVE_COLOR
    return cat

def index(request):
    category_list = list(Category.objects.all())
    home_dummy_cat = get_home_dummy_cat()
    category_list.insert(0, home_dummy_cat)
    website_list = Website.objects.all().order_by('-pub_date')[:settings.HOME_NUM_WEBSITES]
    c = RequestContext(request, {'category_list': category_list, 'act_cat': home_dummy_cat, 'website_list': website_list})
    return render_to_response('website_list.html', c)

def category(request, url_name):
    category_list = list(Category.objects.all())
    home_dummy_cat = get_home_dummy_cat()
    category_list.insert(0, home_dummy_cat)
    act_cat = get_object_or_404(Category, url_name=url_name)
    website_list = act_cat.website_set.all().order_by('order')
    c = RequestContext(request, {'category_list': category_list, 'act_cat': act_cat, 'website_list': website_list})
    return render_to_response('website_list.html', c)

def contact(request):
    category_list = list(Category.objects.all())
    home_dummy_cat = get_home_dummy_cat()
    category_list.insert(0, home_dummy_cat)
    c = RequestContext(request, {'category_list': category_list})
    return render_to_response('contact.html', c)
