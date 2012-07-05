import datetime
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from website_showroom.models import Edition, Category, EditionWebsite, EditionCategory


def get_edition_list():
    editions = Edition.objects.all()
    if len(editions) > 1:
        return editions
    else:
        return []


def get_act_edition(request, ed_country = None):
    eds = Edition.objects.all()
    if len(eds) == 0:
        raise ImproperlyConfigured('There must be at least one edition for the site to work properly.')
    else:
        if ed_country:
            ed = Edition.objects.get(country=ed_country)
            return ed
        else:
            if 'edition' in request.COOKIES:
                ed = Edition.objects.get(country=request.COOKIES['edition'])
                return ed
            else:
                if 'HTTP_ACCEPT_LANGUAGE' in request.META:
                    print request.META['HTTP_ACCEPT_LANGUAGE'][0:2]
                    try:
                        ed = Edition.objects.get(country=request.META['HTTP_ACCEPT_LANGUAGE'][0:2])
                        return ed
                    except ObjectDoesNotExist:
                        pass
                return eds[0]
    

def get_home_dummy_ed_cat(act_edition):
    ed_cat = EditionCategory()
    ed_cat.name = act_edition.home_menu_title
    ed_cat.url_name = ''
    cat = Category()
    cat.color = act_edition.home_menu_color
    cat.active_color = act_edition.home_menu_active_color
    ed_cat.category = cat
    return ed_cat


def get_ed_category_list(act_edition):
    ed_cats = EditionCategory.objects.filter(edition=act_edition)
    return list(ed_cats)


def act_edition_redirect(request):
    act_edition = get_act_edition(request)
    return HttpResponseRedirect("/" + act_edition.country + "/")


def index(request, ed_country):
    act_edition = get_act_edition(request, ed_country)
    ed_category_list = get_ed_category_list(act_edition)
    home_dummy_ed_cat = get_home_dummy_ed_cat(act_edition)
    ed_category_list.insert(0, home_dummy_ed_cat)
    ed_website_list = EditionWebsite.objects.filter(edition=act_edition).order_by('-pub_date')[:act_edition.home_num_websites]
    c = RequestContext(request, {
        'edition_list': get_edition_list(),
        'act_edition': act_edition, 
        'ed_category_list': ed_category_list, 
        'act_ed_cat': home_dummy_ed_cat, 
        'ed_website_list': ed_website_list
    })
    response = render_to_response('website_list.html', c)
    max_age = 250 * 24 * 60 * 60 
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie('edition', ed_country, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
    return response


def category(request, ed_country, url_name):
    act_edition = get_act_edition(request, ed_country)
    ed_category_list = get_ed_category_list(act_edition)
    home_dummy_ed_cat = get_home_dummy_ed_cat(act_edition)
    ed_category_list.insert(0, home_dummy_ed_cat)
    act_ed_cat = get_object_or_404(EditionCategory, url_name=url_name)
    ed_website_list = EditionWebsite.objects.filter(edition=act_edition, website__category=act_ed_cat.category).order_by('order')
    c = RequestContext(request, {
        'edition_list': get_edition_list(),
        'act_edition': act_edition, 
        'ed_category_list': ed_category_list, 
        'act_ed_cat': act_ed_cat, 
        'ed_website_list': ed_website_list
    })
    return render_to_response('website_list.html', c)

def contact(request, ed_country):
    act_edition = get_act_edition(request, ed_country)
    ed_category_list = get_ed_category_list(act_edition)
    home_dummy_ed_cat = get_home_dummy_ed_cat(act_edition)
    ed_category_list.insert(0, home_dummy_ed_cat)
    c = RequestContext(request, {
        'edition_list': get_edition_list(),
        'act_edition': act_edition, 
        'ed_category_list': ed_category_list
    })
    return render_to_response('contact.html', c)
