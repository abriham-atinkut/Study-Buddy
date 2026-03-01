from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),

    path('api/', include('base.api_urls')),
    path('api/token/', obtain_auth_token),
]
