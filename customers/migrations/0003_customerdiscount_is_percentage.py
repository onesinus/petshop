# Generated by Django 3.2.7 on 2021-09-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210910_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdiscount',
            name='is_percentage',
            field=models.BooleanField(default=False),
        ),
    ]
