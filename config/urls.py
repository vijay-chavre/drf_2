from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/", include("core_apps.UserAccount.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # This is your OpenAPI schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI view (replace drf-yasg one)
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),

    # Redoc view
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

]
