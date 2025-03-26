from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, Category, Supplier


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    category = (
        CategorySerializer()
    )  # Use the full serializer or customize it in the serializer class
    supplier = SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_supplier(self, obj):
        return {"id": obj.supplier.id, "name": obj.supplier.name}
