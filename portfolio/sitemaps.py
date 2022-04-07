from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PortfolioSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'resume', 'curriculum_vitae', 'projects']

    def location(self, item):
        return reverse(item)
