from django.db import models
from django.utils.text import slugify



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to='images/categories', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not set
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
class Color_Variant(models.Model):
    color_name=models.CharField(max_length=100)
    
    
    def __str__ (self):
       return self.color_name 
    
        
class Product(models.Model):
    product_name=models.CharField(max_length=200)      
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    image=models.ImageField(blank=True,null=True,upload_to='images/products')
    quantity=models.IntegerField(default=30)
    price=models.CharField(max_length=20)
    color=models.ForeignKey(Color_Variant,on_delete=models.PROTECT,blank=True,null=True)
    description=models.TextField()
    
    
    def __str__ (self):
        return slugify(self.product_name)
    

