from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserAccountViewSet


router = DefaultRouter()
router.register(r"users", UserAccountViewSet, basename="useraccount")
urlpatterns = [
    path("", include(router.urls)),
]
