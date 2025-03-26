from core_apps.UserAccount.views import UserViewSet
from core_apps.Product.views import ProductViewSet, CategoryViewSet, SupplierViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"suppliers", SupplierViewSet, basename="suppliers")
