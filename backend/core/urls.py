from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clicked.urls', namespace='clicked')),
    path('', include('clicked_api.urls', namespace='clicked_api'))
]
