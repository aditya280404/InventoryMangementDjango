from django.contrib import admin
from .models import Customer, Product, Order, OrderProduct

# Register the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    search_fields = ('name', 'user__username')

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity')
    search_fields = ('name',)

# Register the OrderProduct model inline within the Order admin
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'get_customer_name', 'get_customer_id')
    search_fields = ('customer__name', 'customer__user__username')
    inlines = [OrderProductInline]

    def get_customer_name(self, obj):
        return obj.customer.name

    def get_customer_id(self, obj):
        return obj.customer.id

    get_customer_name.short_description = 'Customer Name'
    get_customer_id.short_description = 'Customer ID'
