from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('table/', include('table.urls')),
    path('admin/', admin.site.urls),
]