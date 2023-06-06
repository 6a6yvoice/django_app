from django.db import models

 #Create your models here.
#class User1(models.Model):
#    Email  = models.EmailField(max_length=254)
#    Username = models.CharField(max_length=100)
#    Password = models.CharField(max_length=50)
#    year_of_reg = models.DateField(auto_now=True)


class ProdCategory(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    count = models.IntegerField()


class Product1(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Count = models.IntegerField()
    Article = models.IntegerField()
    cat = models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    pic = models.FileField(upload_to="fapp/static/pic", default=0, null=True)

    def price_in_usd(self):
        return self.Price // 70 
    
    def fullprice(self):
        return self.Price * self.Count



class Invoice(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=256)
    Number = models.IntegerField()
    City = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    House_num = models.IntegerField()
    Apart_num = models.IntegerField()
    prod_article = models.ForeignKey(Product1, on_delete=models.CASCADE)
 

class Cart(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Product1, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
