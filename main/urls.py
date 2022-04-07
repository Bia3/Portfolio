"""
seo app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from .views import CodeOfConductView, PrivacyPolicyView, SecurityPolicyView, AboutView, SiteMapView, robots_txt
from .sitemaps import SeoSitemap
from portfolio.sitemaps import PortfolioSitemap

sitemaps = {
    'main_static': SeoSitemap,
    'portfolio_static': PortfolioSitemap,
}

urlpatterns = [
    path('', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('codeofconduct/', CodeOfConductView.as_view(), name='code_of_conduct'),
    path('privacypolicy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('securitypolicy/', SecurityPolicyView.as_view(), name='security_policy'),
    path('about/', AboutView.as_view(), name='about'),
    path('sitemap/', SiteMapView.as_view(), name='sitemap'),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
