from decimal import Decimal
from unicodedata import name

from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from products.models import Brand, Category, Image, Product

# Create your tests here.

class ProductViewsTest(TestCase,SimpleTestCase):


    def setUp(self):

        self.product = Product.objects.create(name='test',description='Test description')
        self.create_response = self.client.get(reverse('products:create'))
        self.detail_response = self.client.get(self.product.get_absolute_url())
        self.delete_response = self.client.get(reverse('products:delete',kwargs={'slug':self.product.slug}))
        self.list_response = self.client.get(reverse('products:list'))

    def test_product_create_url_name(self):
        
        self.assertEqual(self.create_response.status_code,200)

    def test_product_create_template(self):

        self.assertTemplateUsed(self.create_response,'products/product_create.html')

    
    def test_product_detail_url_name(self):
        
        self.assertEqual(self.detail_response.status_code,200)

    def test_product_detail_template(self):

        self.assertTemplateUsed(self.detail_response,'products/product_detail.html')

    
    
    def test_product_delete_url_name(self):
        
        self.assertEqual(self.delete_response.status_code,200)

    def test_product_delete_template(self):

        self.assertTemplateUsed(self.delete_response,'products/product_delete.html')

    
    def test_product_list_url_name(self):
        
        self.assertEqual(self.list_response.status_code,200)

    def test_product_list_template(self):

        self.assertTemplateUsed(self.list_response,'products/product_list.html')