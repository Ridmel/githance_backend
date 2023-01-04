from django.contrib import admin
from django.urls import include, path

from apps.authentication.urls import urlpatterns as auth_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]

urlpatterns += auth_urls
