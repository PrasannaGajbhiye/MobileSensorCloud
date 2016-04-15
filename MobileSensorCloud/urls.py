from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^user/', include('dashboard.urls')),
    url(r'^sensor_owner/', include('sensor_owner.urls')),
]
