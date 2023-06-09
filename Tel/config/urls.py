from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from api.views import *
# from dj_rest_auth.registration import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', include("main.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)