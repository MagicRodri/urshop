from django.test import TestCase


from products.models import Product
from .models import Cart,CartItem
# Create your tests here.
class TestCart(TestCase):
    def setUp(self) -> None:
        self.cart = Cart.objects.create()

    def test_cart_creation(self):
        self.assertNotEqual(Cart.objects.count(),0)

class TestCartItem(TestCase):
    def setUp(self) -> None:
        cart = Cart.objects.create()
        product = Product.objects.create(name='test',description='Test',quantity=5)
        self.cart_item = CartItem.objects.create(cart = cart,product = product,quantity = 3)

    def test_cart_item_creation(self):
        self.assertNotEqual(CartItem.objects.count(),0)

    def test_cart_item_total(self):
        self.assertTrue(self.cart_item.total == self.cart_item.product.price * self.cart_item.quantity)