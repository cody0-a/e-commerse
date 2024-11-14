from django.db import models


class Category(models.Model):
    prod_type = models.OneToOneField('Product',on_delete=models.CASCADE,related_name='pr')



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
