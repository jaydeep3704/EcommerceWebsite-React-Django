from django.db import models
from users.models import NewUser 


class Shipping(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    postal_code=models.IntegerField()
    address=models.CharField(max_length=300)
    phone_no=models.IntegerField()
    
    
