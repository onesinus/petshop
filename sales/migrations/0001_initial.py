# Generated by Django 3.2.7 on 2021-09-10 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_auto_20210910_1752'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(max_length=15)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_salesorder_created_by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales_salesorder_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'trx_sales_order',
            },
        ),
        migrations.CreateModel(
            name='SalesOrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('qty', models.IntegerField()),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_salesorderdetail_created_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.salesorder')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales_salesorderdetail_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'trx_sales_order_detail',
            },
        ),
    ]
