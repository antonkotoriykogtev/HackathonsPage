from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('reg.urls')),
    path('admin/', admin.site.urls),
     path('accounts/', include('django.contrib.auth.urls')),
     path('accounts/', include('allauth.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
