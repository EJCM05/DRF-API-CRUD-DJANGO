from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autenticationWeb.urls')),
    path('apiExternal', include('projectsApi.urls')),
    
]
