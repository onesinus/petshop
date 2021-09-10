from django.db import models
from _configuration.models import Audit
from customers.models import Customer
from products.models import Product


class SalesOrder(Audit):
    id = models.CharField(max_length=15, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)    
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'trx_sales_order'


class SalesOrderDetail(Audit):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    sales_price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=12, decimal_places=2)
    sub_total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'trx_sales_order_detail'
