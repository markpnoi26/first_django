from django.urls import path
from . import views
# notes taken from the django documentation for media root, and media url
# need to be changed during production
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name="blog-about")
]

# only if settings.DEBUG is true under settings (in development) then we add a static per Django docs.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
