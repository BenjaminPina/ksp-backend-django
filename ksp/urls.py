from django.contrib import admin
from django.urls import path, include

from empleados import urls as empleados_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(empleados_urls)),
]
