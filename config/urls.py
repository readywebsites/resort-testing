from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
import os

DIST_DIR = os.path.join(settings.BASE_DIR, "dist")
ASSETS_DIR = os.path.join(DIST_DIR, "assets")

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API
    path('api/', include('core.urls')),

    # React assets (JS/CSS)
    re_path(
        r'^assets/(?P<path>.*)$',
        serve,
        {'document_root': ASSETS_DIR}
    ),

    # Other root files if needed
    re_path(
        r'^(?P<path>favicon\.svg|icons\.svg)$',
        serve,
        {'document_root': DIST_DIR}
    ),

    # React SPA fallback
    re_path(
        r'^.*$',
        serve,
        {
            'path': 'index.html',
            'document_root': DIST_DIR
        }
    ),
]