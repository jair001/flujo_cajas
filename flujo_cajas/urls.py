from django.urls import path, include

from flujo_cajas.settings import STATIC_URL, MEDIA_URL, STATIC_ROOT, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('flujo/', include('apps.flujo.urls')),
]+static(STATIC_URL, document_root =STATIC_ROOT)

urlpatterns +=static(MEDIA_URL, document_root=MEDIA_ROOT)
