from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('kiphomes/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/profile/', include('profiles.urls')),
    path('api/v1/properties/', include('properties.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Kip Homes Admin'
admin.site.site_title = 'Kip Homes Admin Portal'
admin.site.index_title = 'Welcome to the Kip Homes Portal'