from django.db import models
from users.models import NewUser 
from api.models import Product
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver


class Cart(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    total_price=models.FloatField(default=0)
    
    def __str__(self):
        return self.user.user_name+"'s Cart   Amount:"+str(self.total_price)
    
    
class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(default=0)
    quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.user.user_name)+" "+(self.product.product_name)
        
    
@receiver(pre_save, sender=CartItems)
def my_handler(sender, **kwargs):
    cart_items=kwargs['instance']
    price_of_product=Product.objects.get(id=cart_items.product.id).price
    cart_items.price=cart_items.quantity*float(price_of_product)
    total_cart_items=CartItems.objects.filter(user=cart_items.user)
    cart_items.total_items=len(total_cart_items)
    total_cart_price=0
    for cart_item in total_cart_items:
        total_cart_price+=cart_item.price
  
    cart=Cart.objects.get(user=cart_items.user)
    cart.total_price=total_cart_price
    cart.save()