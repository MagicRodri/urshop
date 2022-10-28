from decimal import Decimal
from unicodedata import name

from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils.text import slugify

from .models import Brand, Category, Image, Product

# Create your tests here.

class CategoryTests(TestCase):


    def setUp(self) -> None:
        self.category = category=Category.objects.create(name='test_category',description='test_description')
        self.category_without_descrtion=Category.objects.create(name='test_category2',slug='cat-slug')

    def test_category_creation(self):
        self.assertEqual(Category.objects.count(),2)
        self.assertEqual(self.category.name,'test_category')
        self.assertEqual(self.category.description,'test_description')

    def test_category_auto_slug(self):
        self.assertFalse(len(self.category.slug) == 0)
        self.assertTrue(self.category.slug == slugify(self.category.name) )

class BranTests(TestCase):


    def test_brand_creation(self):
        brand = Brand.objects.create(name='test_brand')
        self.assertEqual(Brand.objects.count(),1)
        self.assertTrue(brand.name == 'test_brand')

    def test_brand_non_duplication(self):
        brand = Brand.objects.create(name='test_brand')
        # This won't be created
        brand2 = Brand.objects.create(name='Test_brand')
        self.assertEqual(Brand.objects.count(),1)

        with self.assertRaises(Brand.DoesNotExist):
            brand2.refresh_from_db()

class ImageTests(TestCase):
    ...

class ProductTests(TestCase):


    def setUp(self) -> None:
        
        brand = Brand.objects.create(name='test_brand')
        category=Category.objects.create(name='test_category',description='test_description')
        category_without_descrtion=Category.objects.create(name='test_category2')

        self.product = Product.objects.create(name = 'test_product',description = 'test',price = 9.99)
        self.product.brand = brand
        self.product.category.add(category,category_without_descrtion)
        self.product.save()

        self.number = 10
        for i in range(self.number):
            Product.objects.create(name = 'test slug',description = f'test{i}',price = 9.99)


    def test_product_creation(self):
        
        self.assertEqual(self.product.name,'test_product')
        self.assertEqual(self.product.description,'test')
        self.assertEqual(float(self.product.price),9.99)
        self.assertEqual(self.product.brand.name,'test_brand')
        self.assertEqual(self.product.category.count(),2)
        self.assertTrue(self.product.is_active)

    def test_product_slug_auto_creation(self):

        self.assertFalse(self.product.slug=='')
        self.assertTrue(self.product.slug == slugify(self.product.name))

    def test_product_slug_uniqueness(self):

        products = Product.objects.all()
        for product in products:
            query = products.filter(slug = product.slug).exclude(id = product.id)
            self.assertFalse(query.exists())


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
