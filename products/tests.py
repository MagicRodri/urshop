from decimal import Decimal

from django.test import TestCase,SimpleTestCase
from django.urls import reverse

from .models import Product,Brand,Image,Category
# Create your tests here.

class CategoryTests(TestCase):
    def test_category_creation(self):
        category=Category.objects.create(name='test_category',description='test_description')

        category_without_descrtion=Category.objects.create(name='test_category2')

        self.assertEqual(Category.objects.count(),2)
        self.assertEqual(category.name,'test_category')
        self.assertEqual(category.description,'test_description')

class BranTests(TestCase):
    def test_brand_creation(self):
        brand = Brand.objects.create(brand_name='test_brand')

        self.assertEqual(Brand.objects.count(),1)
        self.assertTrue(brand.brand_name == 'test_brand')

class ImageTests(TestCase):
    ...

class ProductTests(TestCase):
    def setUp(self) -> None:
        brand = Brand.objects.create(brand_name='test_brand')
        category=Category.objects.create(name='test_category',description='test_description')
        category_without_descrtion=Category.objects.create(name='test_category2')

        product = Product.objects.create(name = 'test_product',description = 'test',price = 9.99)
        product.brand = brand
        product.category.add(category,category_without_descrtion)
        product.save()

    def test_product_creation(self):

        product = Product.objects.get(name='test_product')
        
        self.assertEqual(product.name,'test_product')
        self.assertEqual(product.description,'test')
        self.assertEqual(float(product.price),9.99)
        self.assertEqual(product.brand.brand_name,'test_brand')
        self.assertEqual(product.category.count(),2)
        self.assertTrue(product.is_active)


class CreatePageTest(TestCase,SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse('products:create'))

    def test_product_create_url_name(self):
        
        self.assertEqual(self.response.status_code,200)

    def test_product_create_template(self):
        self.assertTemplateUsed(self.response,'products/create_product.html')