from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/',include('booking.urls')),
    path('',include('root.urls')),
    path('admin_area/',include('admin_site.urls')),
    path('plan/',include('plan.urls')) 
]
if settings.DEBUG :
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)