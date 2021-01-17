from django.db import models
from orders.models import BaseOrder
from product.models import BaseProduct
# # Create your models here.
class BaseOrderIetms(models.Model):
    order = models.ForeignKey(BaseOrder,  on_delete=models.CASCADE)
    product = models.ForeignKey(BaseProduct,  on_delete=models.CASCADE)
    quantity = models.IntegerField()
    