from django.test import TestCase

from fapp.models import *

class ProductTestCase(TestCase):
    def setUp(self):
        ProdCategory.objects.create(category_name = "prodcat1", description = "desc", count = 2)
        ProdCategory.objects.create(category_name = "prodcat2", description = "desc2", count = 4)
        Product1.objects.create(Name = "Product", Description = "product descrip", Price = 4900, Count = 2, Article = 123, cat = ProdCategory(1))
        Product1.objects.create(Name = "Product2", Description = "product descrip2", Price = 70000, Count = 2, Article = 321, cat = ProdCategory(1))
    def test_convert_to_usd(self):
        prod1 = Product1.objects.get(Name = "Product")
        prod2 = Product1.objects.get(Name = "Product2")
        self.assertEqual(prod1.price_in_usd(), 70)
        self.assertEqual(prod2.price_in_usd(), 1000)
    

