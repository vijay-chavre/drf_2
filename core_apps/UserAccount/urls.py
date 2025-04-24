from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserAccountViewSet, ChangePasswordView

# Create router and register ViewSets only
router = DefaultRouter()
router.register(r"users", UserAccountViewSet, basename="useraccount")

# Define final URL patterns
urlpatterns = [
    path("", include(router.urls)),  # Handles /users/ (ViewSet routes)
    path("change-password/", ChangePasswordView.as_view(),
         name="change-password"),  # Handles /change-password/
]
