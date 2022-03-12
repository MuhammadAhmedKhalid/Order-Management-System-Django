from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    pro_quantity = models.IntegerField(default=0)
    pro_price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/user/media/')

    def __str__(self):
        return self.name

class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption

class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    ord_quantity = models.IntegerField(default=0)
    ord_price = models.IntegerField(default=0)
