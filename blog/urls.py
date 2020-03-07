from django.urls import path
from . import views
from . views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
# notes taken from the django documentation for media root, and media url
# need to be changed during production
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="blog-about")
]

# only if settings.DEBUG is true under settings (in development) then we add a static per Django docs.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
