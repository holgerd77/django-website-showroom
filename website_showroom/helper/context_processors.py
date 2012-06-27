from django.conf import settings

# Makes showroom settings available in templates
def showroom(request):
    return {
        "HTML_TITLE": settings.HTML_TITLE,
        "SITE_TITLE": settings.SITE_TITLE,
        "SITE_SUBTITLE": settings.SITE_SUBTITLE,
        "RSS_TITLE": settings.RSS_TITLE,
        "FACEBOOK_URL": settings.FACEBOOK_URL,
        "FOOTER_LEFT": settings.FOOTER_LEFT,
        "FOOTER_RIGHT": settings.FOOTER_RIGHT,
        "CONTACT_TITLE": settings.CONTACT_TITLE,
        "CONTACT_HTML": settings.CONTACT_HTML,
    }
