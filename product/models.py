from django.db import models



class Color(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Yaddas(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'TITLE')
    price = models.PositiveIntegerField(default=0)
    discount = models.IntegerField(null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    cover_image = models.ImageField(upload_to='product/', null=True, blank=True)

    color = models.ManyToManyField(Color) 
    yaddas = models.ManyToManyField(Yaddas, blank=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductProperty(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.key}: {self.value}"
