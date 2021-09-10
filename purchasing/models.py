from django.db import models
from _configuration.models import Audit
from products.models import Product


class PurchaseOrder(Audit):
    id = models.CharField(max_length=15, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    capital_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'trx_purchase_order'

