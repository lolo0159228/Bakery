from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    productID = models.AutoField(max_length=10,primary_key=True)
    name = models.CharField(max_length=50)
    pric = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    img = models.ImageField(upload_to='product/static/IMG')

    createdate = models.DateTimeField(default=timezone.now)
    stopdate = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return str(self.productID) +'__'+ (self.name)

    class Meta:
        ordering = ['productID']