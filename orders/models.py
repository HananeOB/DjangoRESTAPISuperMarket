from django.db import models
from django.contrib.auth.forms import User
from product.models import BaseProduct 
# # Create your models here.
class BaseOrder(models.Model):
    customer = models.ForeignKey(User,  on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)


