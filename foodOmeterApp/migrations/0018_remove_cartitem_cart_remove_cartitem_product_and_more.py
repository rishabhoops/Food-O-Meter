# Generated by Django 4.2 on 2023-06-01 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0017_cart_cartitem_cart_products_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]