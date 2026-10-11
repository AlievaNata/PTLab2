from django.core.management import call_command
from django.test import TestCase

from shop.models import Category, Product


class ProductsFixtureTestCase(TestCase):
    fixtures = ['products.yaml']

    def test_categories_are_loaded(self):
        self.assertEqual(
            set(Category.objects.values_list('name', flat=True)),
            {'Диваны', 'Кресла', 'Пуфы и банкетки', 'Кушетки'})

    def test_products_are_loaded(self):
        self.assertEqual(Product.objects.count(), 12)

    def test_every_category_has_products(self):
        for category in Category.objects.all():
            self.assertTrue(category.products.exists(), category.name)

    def test_every_product_is_complete(self):
        for product in Product.objects.all():
            self.assertIsNotNone(product.category, product.name)
            self.assertGreater(product.price, 0, product.name)
            self.assertTrue(product.description, product.name)

    def test_product_names_are_unique(self):
        names = list(Product.objects.values_list('name', flat=True))
        self.assertEqual(len(names), len(set(names)))

    def test_loading_twice_does_not_duplicate_data(self):
        call_command('loaddata', 'products.yaml', verbosity=0)
        self.assertEqual(Product.objects.count(), 12)
        self.assertEqual(Category.objects.count(), 4)
