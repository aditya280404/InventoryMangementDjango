from rest_framework import serializers
from .models import Customer, Product, Order, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
