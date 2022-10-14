from django.core.exceptions import ValidationError
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from products.models import Product

from .models import Cart, CartItem

# Create your tests here.

class TestCart(TestCase):
    def setUp(self) -> None:
        self.cart = Cart.objects.create()

    def test_cart_creation(self):
        self.assertNotEqual(Cart.objects.count(),0)

class TestCartTemplate(TestCase,SimpleTestCase):

    def test_cart_detail_template(self):
        self.assertTemplateUsed('carts/cart_detail.html')

    
    def test_cart_detail_url(self):
        response = self.client.get(reverse('carts:detail'))
        self.assertTrue(response.status_code == 200)

class TestCartItem(TestCase):
    def setUp(self) -> None:
        self.cart = Cart.objects.create()
        self.product = Product.objects.create(name='test',description='Test',quantity=10)
        self.cart_item = CartItem.objects.create(cart = self.cart,product = self.product,quantity = 3)

    def test_cart_item_creation(self):
        self.assertNotEqual(CartItem.objects.count(),0)

    def test_cart_item_total(self):
        self.assertTrue(self.cart_item.total == self.cart_item.product.price * self.cart_item.quantity)

    def test_cart_item_quantity_validator(self):
        item = self.cart_item
        item.quantity = 11
        with self.assertRaises(ValidationError):
            item.save()

    def test_cart_item_quantity_incrementation(self):
        item = self.cart_item
        item.increment()
        self.assertEqual(item.quantity,4)
        item.increment(2)
        self.assertEqual(item.quantity,6)

    # def test_cart_update_on_save(self):
    #     # this won't be created
    #     cart_item = CartItem.objects.create(cart = self.cart,product = self.product,quantity = 2)
    #     cart_item2 = CartItem.objects.create(cart = self.cart,product = self.product,quantity = 2)
    #     self.assertEqual(cart_item.quantity , 4) # 2 + 2