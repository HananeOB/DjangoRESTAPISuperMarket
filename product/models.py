from django.db import models

# Create your models here.
class BaseProduct(models.Model):
    DISCOUNT_CHOICES = (( "a", '50% discount'), ("b", '1 free for 2'), ("c", "No discount"))
    name = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_quantity = models.IntegerField(default=0)
    discounts = models.CharField(max_length=30, choices=DISCOUNT_CHOICES, default="c")

    def __str__(self):
        return self.name 