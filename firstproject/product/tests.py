from django.test import TestCase
from.models import product
# Create your tests here.


class productTest(TestCase):
    def setUp(self):
        self.product=product.pm.create(pro_name="TestProduct",
                          pro_desc="Product has been created for testing",
                           pro_Brand="TestBrand",
                           pro_Price=500)
        

    def test_create_product(self):
        products=product.pm.get(pro_name="TestProduct")
        self.assertEqual(products.id,self.product.id)


    def test_update_product(self):

        products=product.pm.get(pro_name="TestProduct")
        products.pro_Price=2000
        products.save()





        self.assertNotEqual(products.pro_Price,self.product.pro_Price)


        
        
def test_fetch_product(self):
    products=product.pm.all()
    count=len(product)
    self.assertGreater(count,0)
