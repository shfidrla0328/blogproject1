from django.contrib import admin
from django.urls import path, include
import mainapp.urls
import mainapp.views
import accounts.urls
import accounts.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.home, name="home"),
    path('mainapp/', include('mainapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/portfolio', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
