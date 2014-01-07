from django.contrib import admin
from erp_app.models import Customer, General_Setting, Product, Order, Orders_Product


class Orders_ProductInline(admin.TabularInline):
    model = Orders_Product
    extra = 5

class OrderAdmin(admin.ModelAdmin):
    inlines = [Orders_ProductInline]




# Register your models here.

admin.site.register(Customer)
admin.site.register(General_Setting)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
