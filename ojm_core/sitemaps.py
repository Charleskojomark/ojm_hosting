# your_app/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        # List of URL names for your static views
        return ['ojm_core:index', 'userauth:sign', 'userauth:login']

    def location(self, item):
        return reverse(item)
