from django.db import models
from user_app.models import Account
from Common.model.Common import CommonModel 


class TypeModel(CommonModel):
    name = models.CharField(max_length=150, unique=True, blank=False)


class SeasonModels(CommonModel):
    name = models.CharField(max_length=150, unique=True, blank=False)


class ProductModel(CommonModel):
    type_product = models.ForeignKey(TypeModel, on_delete=models.CASCADE)
    season = models.ForeignKey(SeasonModels, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=False)
    amount = models.IntegerField(default=0)
    sale_price = models.FloatField()
    cost_price = models.FloatField()


class OrderModel(CommonModel):
    id_user = models.ForeignKey(Account, on_delete=models.CASCADE) 
    cost_total = models.FloatField()
    status = models.CharField(max_length=150, unique=True)


class Order_ProductModel(CommonModel):
    id_order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    id_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

