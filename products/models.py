from django.db import models
from _configuration.models import Audit


class Product(Audit):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    sales_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'mst_product'


class ProductDetail(Audit):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    capital_price = models.DecimalField(max_digits=12, decimal_places=2)
    expired_date = models.DateField()

    class Meta:
        db_table = 'mst_product_detail'
