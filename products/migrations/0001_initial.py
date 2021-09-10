# Generated by Django 3.2.7 on 2021-09-10 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_product_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products_product_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mst_product',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('qty', models.IntegerField()),
                ('capital_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('expired_date', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_productdetail_created_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products_productdetail_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mst_product_detail',
            },
        ),
    ]