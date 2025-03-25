from django.contrib import admin
from order_app.model.Product import ProductModel, Order_ProductModel, SeasonModels, TypeModel, OrderModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(Order_ProductModel)
admin.site.register(SeasonModels)
admin.site.register(TypeModel)
admin.site.register(OrderModel)

