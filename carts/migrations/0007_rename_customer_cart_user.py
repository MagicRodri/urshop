# Generated by Django 4.1.1 on 2022-10-13 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_cart_is_active_cartitem_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customer',
            new_name='user',
        ),
    ]
