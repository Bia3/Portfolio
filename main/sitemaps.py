from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class SeoSitemap(Sitemap):
    changefreq = "yearly"
    priority = 1.0

    def items(self):
        return ['seo:code_of_conduct', 'seo:privacy_policy', 'seo:security_policy']

    def location(self, item):
        return reverse(item)
