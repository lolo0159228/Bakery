from django.db import models
from django.utils import timezone
from member.models import Member
from product.models import Product
# Create your models here.

class OrderM(models.Model):
    orderID = models.CharField(max_length=12, primary_key=True, unique=True, blank=False)
    user = models.ForeignKey(to=Member,on_delete=models.CASCADE)
    samt = models.IntegerField()
    sqty = models.IntegerField()
    createdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.orderID

    class Meta:
        ordering = ['orderID']

class OrderD(models.Model):
    orderID = models.ForeignKey(to=OrderM,on_delete=models.CASCADE)
    productID = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    productname = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amt = models.IntegerField()

    def __str__(self):
        return str(self.orderID)+'___'+str(self.productID)

    class Meta:
        ordering = ['orderID','productID']
