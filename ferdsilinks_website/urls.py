from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap

from django.conf import settings
from django.conf.urls.static import static

from blog.sitemaps import BlogPostSitemap
from pages.sitemaps import StaticViewSitemap

sitemaps = {
    "posts": BlogPostSitemap,
    "static": StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Pages...
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('download/', include('download.urls')),

    # Sitemaps...
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                        name='django.contrib.sitemaps.views.sitemap')
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)