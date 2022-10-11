import random

from django.test import TestCase

from carts.models import Cart
from .models import Order,Address
# Create your tests here.


class TestAddress(TestCase):

    def test_address_creation(self):
        address = Address.objects.create(
            name = 'test',
            address_line_1 = 'somewhere',
            country = 'Test',
            city = 'test',
            zip = 0000
        )

        self.assertTrue(Address.objects.count() == 1)


class TestOrder(TestCase):

    def setUp(self) -> None:

        self.address = Address.objects.create(
            name = 'test',
            address_line_1 = 'somewhere',
            country = 'Test',
            city = 'test',
            zip = 0000
        )

        self.cart = Cart.objects.create()

        self.order_number = 10
        for _ in range(self.order_number):
            Order.objects.create(
            address = self.address,
            cart = self.cart
        )
    def test_order_creation(self):

        self.assertEqual(Order.objects.count(),self.order_number)

    def test_order_default_status(self):
        
        for order in Order.objects.all():
            self.assertEqual(order.status, order.CREATED)