from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from website_showroom.models import Edition, Category, EditionWebsite

def get_edition():
    eds = Edition.objects.all()
    if len(eds) == 0:
        raise ImproperlyConfigured('There must be at least one edition for the site to work properly.')
    else:
        return eds[0]

def get_home_dummy_cat(edition):
    cat = Category()
    cat.name = edition.home_menu_title
    cat.url_name = ''
    cat.color = edition.home_menu_color
    cat.active_color = edition.home_menu_active_color
    return cat

def index(request):
    edition = get_edition()
    category_list = list(Category.objects.all())
    home_dummy_cat = get_home_dummy_cat(edition)
    category_list.insert(0, home_dummy_cat)
    ed_website_list = EditionWebsite.objects.filter(edition=edition).order_by('-pub_date')[:edition.home_num_websites]
    c = RequestContext(request, {
        'edition': edition, 
        'category_list': category_list, 
        'act_cat': home_dummy_cat, 
        'ed_website_list': ed_website_list
    })
    return render_to_response('website_list.html', c)


def category(request, url_name):
    edition = get_edition()
    category_list = list(Category.objects.all())
    home_dummy_cat = get_home_dummy_cat(edition)
    category_list.insert(0, home_dummy_cat)
    act_cat = get_object_or_404(Category, url_name=url_name)
    ed_website_list = EditionWebsite.objects.filter(edition=edition, website__category=act_cat).order_by('-pub_date')
    c = RequestContext(request, {'edition': edition, 'category_list': category_list, 'act_cat': act_cat, 'ed_website_list': ed_website_list})
    return render_to_response('website_list.html', c)

def contact(request):
    edition = get_edition()
    category_list = list(Category.objects.all())
    home_dummy_cat = get_home_dummy_cat(edition)
    category_list.insert(0, home_dummy_cat)
    c = RequestContext(request, {'edition': edition, 'category_list': category_list})
    return render_to_response('contact.html', c)
