from django.contrib import admin
from django.urls import path, URLPattern, URLResolver, include

urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls'))
]
