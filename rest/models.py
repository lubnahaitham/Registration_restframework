from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default=0)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['-first_name']
    
    def __str__(self):
        return self.first_name
    
class Seller(models.Model):
    name = models.CharField(max_length=255)
    product_size = models.IntegerField()
    
    class Meta:
        ordering = ['-name']
        
        
    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    seller = models.ManyToManyField(Seller)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_query_name='users', null=True, blank=True)
    
    class Meta:
        ordering = ['-price']
    
