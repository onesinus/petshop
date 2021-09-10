from django.db import models
from _configuration.models import Audit
from products.models import Product


class Customer(Audit):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=2048)

    class Meta:
        db_table = 'mst_customer'


class CustomerDiscount(Audit):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    discount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'mst_customer_discount'
    